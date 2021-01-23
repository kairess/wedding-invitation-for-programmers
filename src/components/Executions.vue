<template>
  <div class="executions">
    <!--명령어-->
    <p class="code" v-for="(execution, index) in executions" :key="index" v-show="execution.visible">
      <span class="addon">~</span>
      [<span class="time">{{ execution.time }}</span>]
      <span class="task">{{ execution.name }}</span>
      <span class="duration" v-if="execution.duration!==undefined">{{ execution.duration }} ms</span>
    </p>
    <!--진행도-->
    <p class="code" v-show="isProcessed">
      <span class="addon">~</span>
      {{ progressBarText }}
      <span class="percentage">{{ percentage }}%</span>
    </p>
    <!--명령어-->
    <p class="code" v-show="endExecution.visible">
      <span class="addon">~</span>
      [<span class="time">{{ endExecution.time }}</span>]
      <span class="task">{{ endExecution.name }}</span>
    </p>
  </div>
</template>

<script>
  import data from '../mock/data'
  export default {
    name: 'Executions',
    props: ['canExecute'],
    data () {
      return {
        executions: data.executions,
        isProcessed: false,
        isFinished: false,
        progressBarText: '--------------------------',
        endExecution: {
          name:'여는중...',
          time: '',
          visible: false
        }
      }
    },
    computed: {
      percentage () {
        const hashL = this.progressBarText.split('').filter(c => c==='#').length
        const l = this.progressBarText.length
        return Math.floor(hashL*100/l)
      }
    },
    watch: {
      canExecute: function (val) {
        if (val===true) {
          this.runExecutions()
        }
      }
    },
    updated() {
      this.$emit('onUpdating')
    },
    methods: {
      // 명령어
      runExecutions: async function () {
        for (const execution of this.executions) {
          await this.progressivelyRun(execution)
        }
        // 명령이 실행되면 진행도를 표시한다
        await this.successProcessing(1000)
        // 마지막 명령 실행
        await this.progressivelyRun(this.endExecution)
          .then(() => {
            setTimeout(() => {
              this.isFinished = true
              this.$emit('onFinish')
            }, 500)
          })
      },
      // 명령 진행
      progressivelyRun(execution, customDuration) {
        return new Promise((resolve) => {
          let now = new Date(),
              duration = customDuration ? customDuration : Math.random()*50+250,
              showCode = () => {
                execution.time = now.toLocaleTimeString()
                execution.duration = execution.duration !== undefined ? duration.toFixed(2) : undefined
                execution.visible = true
                resolve()
              }
          setTimeout(showCode, duration)
        })
      },
      // 진행표시줄 보이기
      successProcessing(duration){
        return new Promise((resolve) => {
          let start = null, progressing, progressingCount = 0
          this.isProcessed = true
          let step = (timestamp) => {
              let timeGap
              if (start === null) {
                start = timestamp
              }
              timeGap = timestamp - start
              if (progressingCount%3 === 0) {
                this.progressBarText = this.progressBarText.replace('-', '#')
              }
              progressingCount++
              if (timeGap < duration) {
                progressing = requestAnimationFrame(step)
              } else {
                resolve()
                this.progressBarText = this.progressBarText.replace(/-/g, '#')
                cancelAnimationFrame(progressing)
              }
            }
          progressing = requestAnimationFrame(step)
        });
      }
    }
  }
</script>

<style lang="less">
  .executions{
    .addon{
      color: #68FCFB;
    }
    .time{ color: #666; }
    .task{ color: #009AB2; }
    .duration{
      margin-left: 10px;
      color: #BF36B7;
    }
  }
</style>