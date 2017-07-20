'use strict'
import React, { Component } from 'react'
import PropTypes from 'prop-types'
import Cropper from 'react-cropper'

import 'cropperjs/dist/cropper.css'

import style from './style.scss?module'

export default class EditThumbnail extends Component {
  static propTypes = {
    url: PropTypes.string.isRequired,
    thumbnail: PropTypes.object.isRequired,
    onCancel: PropTypes.func,
    onSave: PropTypes.func,
  }

  state = {
    preview: undefined
  }

  onCropHandler = () => {
    this.setState(this.cropper.getCroppedCanvas().toDataURL())
  }

  onCancelHandler = () => {
    if (this.props.onCancel) {
      this.props.onCancel()
    }
  }

  onSaveHandler = () => {
    const cropData = this.cropper.getData()
    console.log(cropData)
    if (this.props.onSave) {
      this.props.onSave({crop: cropData})
    }
  }

  renderCropper () {
    const {url, thumbnail: {url: thumbnail_url, options}} = this.props
    const {size: [width, height], thumbnail_option_id, crop} = options


    return <Cropper
      ref={(c) => {this.cropper = c}}
      src={url}
      style={{height: 400, width: '100%'}}
      data={crop}
      preview={`.${style.cropPreview}`}
      aspectRatio={width / height}
      rotatable={false}
      dragMode='move'
      viewMode={1}
    />
  }

  render () {
    const {thumbnail: {url: thumbnail_url}} = this.props
    return (
      <div className={style.container}>
        <div className={style.cropper}>
          {this.renderCropper()}
        </div>
        <div className={style.previewList}>
          <div className={style.previewItem}>
            <h2>Old thumbnail</h2>
            <img src={`${thumbnail_url}?r=${new Date().getTime()}`} alt=""/>
          </div>
          <div className={style.previewItem}>
            <h2>New thumbnail</h2>
            <div className={style.cropPreview}/>
          </div>
        </div>
        <div>
          <button onClick={this.onCancelHandler}>Cancel</button>
          <button onClick={this.onSaveHandler}>Save</button>
        </div>
      </div>
    )
  }
}
