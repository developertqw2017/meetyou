import weSwiper from '../../src/main'

var util = require('../../util/util.js')

const SAVE_VOICE = "保存录音"

var playTimeInterval
var recordTimeInterval

Page({
  onReady: function(e) {
    // 使用 wx.createAudioContext 获取 audio 上下文 context
    this.audioCtx = wx.createAudioContext('myAudio')
  },
  data: {
    recording: false,
    playing: false,
    hasRecord: false,
    recordTime: 0,
    playTime: 0,
    formatedRecordTime: '00:00:00',
    formatedPlayTime: '00:00:00',
    saveVoice: SAVE_VOICE
  },
  startRecord: function() {
    this.setData({
      recording: true
    })

    var that = this
    recordTimeInterval = setInterval(function() {
      var recordTime = that.data.recordTime += 1
      that.setData({
        formatedRecordTime: util.formatTime(that.data.recordTime),
        recordTime: recordTime
      })
    }, 1000)

    wx.startRecord({
      success: function(res) {

        // @ tempFilePath: wxfile://    本地临时录音的路径
        // @ errMsg:  startRecord : ok  应该是返回信息
        that.setData({
          hasRecord: true,
          tempFilePath: res.tempFilePath,
          formatedPlayTime: util.formatTime(that.data.playTime)
        })
      },
      complete: function() {
        that.setData({
          recording: false
