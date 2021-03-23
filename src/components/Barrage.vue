<template>
  <div class="wedding-barrage" ref="barrage" :style="{display: canStart ? 'block' : 'none'}">
    <div v-html="codeInStyleTag"></div>
    <p class="code">
      <span class="mine">축복의 한 마디</span>
    </p>
    <p class="code" v-for="(item, index) in barrages" :key="index">
      <span>{{ item.barrage }} <small>{{ item.createdAt }}</small></span>
    </p>
    <p class="code" v-if="wish">
      <span class="mine2">{{ wish }} <small>{{ wishCreatedAt }}</small></span>
    </p>
    <div class="barrage-space"></div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['wish', 'wishCreatedAt', 'canStart'],
    data(){
      return {
        barrages: [],
        animationStyle:'',
        initialOffset: 0
      }
    },
    mounted () {
      axios.get('/barrages').then(response => (
        this.barrages = response.data
      ))
    },
    computed: {
      codeInStyleTag: function () {
        return `<style>${this.animationStyle}</style>`
      }
    },
    // watch: {
    //   canStart: function (val) {
    //     if (val===true) {
    //       this.barrageAnimationStart()
    //     }
    //   }
    // },
    methods: {
      // 팝업 애니메이션 시작
      barrageAnimationStart() {
        let barrageWidth = this.getWidth(this.$refs.barrage)
        let barrageWidthGroup = [
              this.getWidth(this.$refs.barrageFirst),
              this.getWidth(this.$refs.barrageSecond),
              this.getWidth(this.$refs.barrageThird),
              this.getWidth(this.$refs.barrageFourth)
            ]
        this.initialOffset = barrageWidth + 15
        barrageWidthGroup.map((item,index) => {
          this.animationStyle += `
            .barrage-${index}{
              animation: barrage-${index} ${item/40}s linear infinite;
              -webkit-animation: barrage-${index} ${item/40}s linear infinite;
            }
            @keyframes barrage-${index} {
              from {
                transform:translate3d(${barrageWidth+15}px,0,0);
                -webkit-transform:translate3d(${barrageWidth+15}px,0,0);
              }
              to {
                transform:translate3d(-${item+15}px,0,0);
                -webkit-transform:translate3d(-${item+15}px,0,0);
              }
            }`
        })
      },
      getWidth(ref) {
        return window.getComputedStyle(ref,null).width.replace('px','') - 0
      },
      filterBarrage(barrages, remainder) {
        if(barrages){
          return barrages.filter((barrage, index) => {
            if(index%4 === remainder){
              return barrage
            }
          })
        }
      }
    }
  }
</script>

<style lang="less">
  .wedding-barrage{
    position: relative;
    padding-top: 20px;
    p{
      position: relative;
      padding: 5px 0;
      // white-space:nowrap;
      // transition: all 0.6s linear;
      // -webkit-transition: all 0.6s linear;
      span{
        padding: 0 15px;
        font-size: 16px !important;
        &.mine{
          color: #e6db74;
          padding: 3px 10px;
          border: 1px solid #e6db74;
        }
        &.mine2{
          color: #e6db74;
        }
      }
    }
    .barrage-space{
      height: 180px;
    }
  }
</style>