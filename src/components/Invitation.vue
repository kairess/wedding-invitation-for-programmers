<template>
  <div class="wedding-invitation" :class="{ 'invitation-bounce':canOpen }">
    <div class="invitation-container" :class="{ 'invitation-down':isOpening }">
      <div class="invitation-cover">
        <div class="cover-content" :class="{'invitation-up':isOpening}">
          <div class="content-inside">
            <!-- <video ref="video" loop>
              <source src="../images/video.mp4" type="video/mp4">
              다른 브라우저로 열어주세요!
            </video> -->
            <img class="content-inside-photo" src="../images/10.jpeg">
            <p>우리 결혼합니다！</p>
            <p><b>이희수 & 이태희</b></p>
            <p>시간：2021년 5월 8일 오후 2시</p>
            <p>장소：<b>용산가족공원 연못광장</b></p>
            <p>주차：<b>국립중앙박물관 주차장</b></p>
            <div class="content-inside-bless">
              <input
                placeholder="여기를 눌러 축복의 한 마디를 입력해주세요" 
                @keyup.enter="sendBarrage"
                @focus="isFocused = true"
                @blur="isFocused = false, hasEntered = false"
                v-model="wish"
                ref="wishInput"
              >
              <p v-if="!wish && isFocused && hasEntered">축복을 입력해주세요!</p>
              <div>
                <button @click="sendBarrage">보내기</button>
                <button @click="closeInvitation">닫기</button>
              </div>
              <div>
                <a href="https://qr.kakaopay.com/281006011000078669865552" target="_blank" class="button">
                  결혼식 후원하기
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="cover-inside-left" :class="{'opening':isOpening}"></div>
        <div class="cover-inside-right" :class="{'opening':isOpening}"></div>
        <img class="cover-inside-seal" src="../images/seal.png" @click="openInvitation" :class="{'invitation-flight':isOpening}">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
var querystring = require('querystring')

export default {
  props: ['canOpen'],
  data() {
    return {
      isOpening: false,
      wish: '',
      isFocused: false,
      hasEntered: false
    }
  },
  methods: {
    // 초대장 열기
    openInvitation(){
      this.isOpening = true
      // this.$refs.video.play()
    },
    closeInvitation () {
      this.isOpening = false
      // this.$refs.video.pause()
      setTimeout(() => {
        this.$emit('onClose')
      }, 660)
    },
    // 축하 탄막 발송
    sendBarrage(){
      this.$nextTick(() => {
        this.hasEntered = true
        if (!this.wish) {
          return
        }

        axios.post('/barrage', querystring.stringify({
          'barrage': this.wish
        }))

        this.isOpening = false
        this.$refs.wishInput.blur()
        setTimeout(() => {
          this.$emit('sendBarrage', this.wish)
        }, 660)
      })
    }
  }
}
</script>

<style lang="less">
  a.button {
    text-decoration: none;
    width: 100%;
    height: 35px;
    color: #a9895d;
    outline: none;
    margin-top: 6px;
    border: 1px solid #f7debb;
    background: transparent;
    flex: 1;
    vertical-align: middle;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  a.button:hover {
    color: #a9895d;
  }

  video {
    width: 100%;
  }

  .wedding-invitation{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding: 30px 20px;
    padding-top: 60px;
    z-index: 4;
    transform: scale(0.05);
    -webkit-transform: scale(0.05);
    opacity: 0;
    transition: transform 0.8s cubic-bezier(.26,1.84,.39,.61), opacity 0.5s linear;
    -webkit-transition: -webkit-transform 0.8s cubic-bezier(.26,1.84,.39,.61), opacity 0.5s linear;
    background-size: 100%;
    overflow: hidden;
    &.invitation-bounce{
      opacity: 1;
      transform: scale(1);
      -webkit-transform: scale(1);
    }
    .invitation-container{
      position: relative;
      width: 100%;
      height: 100%;
      transition: transform 0.6s cubic-bezier(0.4, 0, 1, 1);
      -webkit-transition: -webkit-transform 0.6s cubic-bezier(0.4, 0, 1, 1);
      &.invitation-down{
        transform: translateY(20px);
        -webkit-transform: translateY(20px);
      }
      .invitation-cover{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #f7decb;
        border-radius: 10px;
        perspective: 500px;
        box-shadow: 0 0 20px 2px rgba(0, 0, 0, 0.15);
        .cover-content{
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          padding: 10px 20px;
          transition: transform 0.6s cubic-bezier(0.4, 0, 1, 1);
          -webkit-transition: -webkit-transform 0.6s cubic-bezier(0.4, 0, 1, 1);
          &.invitation-up{
            transform: translateY(-60px);
            -webkit-transform: translateY(-60px);
          }
          .content-inside{
            height: 100%;
            padding: 20px;
            color: #a9895d;
            background-color: #FFF1DE;
            text-align: center;
            overflow: auto;
            .content-inside-photo{
              width: 100%;
              margin-bottom: 10px;
              padding: 5px;
              border: 1px solid #f7debb;
            }
            p{
              margin-top: 0;
              margin-bottom: 5px;
            }
            .content-inside-bless{
              input{
                width: 100%;
                height: 35px;
                margin-bottom: 10px;
                outline: none;
                border: none;
                border-bottom: 1px solid #f7debb;
                color: #a9895d;
                background: transparent;
                &::-webkit-input-placeholder { color: #a9895d;font-size: 12px; }
                &::-moz-placeholder { color: #a9895d;font-size: 12px; }
                &:-ms-input-placeholder { color: #a9895d;font-size: 12px; }
                &:-moz-placeholder { color: #a9895d;font-size: 12px; }
              }
              >div{
                display: flex;
                button{
                  width: 100%;
                  height: 35px;
                  color: #a9895d;
                  background: #f7debb;
                  border: none;
                  outline: none;
                  &:disabled{
                    opacity: 0.8;
                  }
                  &:first-child{
                    margin-right: 10px;
                    flex: 1;
                  }
                  &:last-child{
                    width: 60px;
                    border: 1px solid #f7debb;
                    background: transparent;
                  }
                }
              }
            }
          }
        }
        .cover-inside-left{
          position: absolute;
          left: 0;
          top: 0;
          width: 70%;
          height: 100%;
          border-radius: 10px;
          background-color: #f7decb;
          box-shadow: 5px 0 10px rgba(0,0,0,0.2);
          z-index: 6;
          transition: transform 0.5s;
          -webkit-transition: -webkit-transform 0.5s;
          transform-origin: 0 50%;
          -webkit-transform-origin: 0 50%;
          &.opening{
            transform: rotate3d(0,1,0,-140deg);
            -webkit-transform: rotate3d(0,1,0,-140deg);
          }
        }
        .cover-inside-right{
          position: absolute;
          right: 0;
          top: 0;
          width: 40%;
          height: 100%;
          border-radius: 10px;
          background-color: #f7decb;
          box-shadow: -5px 0 10px rgba(0,0,0,0.2);
          z-index: 5;
          transition: transform 0.5s;
          -webkit-transition: -webkit-transform 0.5s;
          transform-origin: 100% 50%;
          -webkit-transform-origin: 100% 50%;
          &.opening{
            transform: rotate3d(0,1,0,140deg);
            -webkit-transform: rotate3d(0,1,0,140deg);
          }
        }
        .cover-inside-seal{
          position: absolute;
          left: 70%;
          bottom: 100px;
          width: 80px;
          height: 80px;
          margin-left: -40px;
          z-index: 7;
          transform-origin: 50% 50%;
          -webkit-transform-origin: 50% 50%;
          transition: all 0.8s cubic-bezier(0.4, 0, 1, 1);
          -webkit-transition: all 0.8s cubic-bezier(0.4, 0, 1, 1);
          &.invitation-flight{
            opacity: 0;
          }
        }
      }
    }
  }
</style>
