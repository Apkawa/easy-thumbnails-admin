'use strict'
import React, { Component } from 'react'
import PropTypes from 'prop-types'

import $ from 'jquery'
import csrfSetup from '../csrf'
csrfSetup()

import InfoDisplay from '../InfoDisplay'
import EditThumbnail from '../EditThumbnail'

export  default  class Info extends Component {
  static propTypes = {
    name: PropTypes.string.isRequired,
    target: PropTypes.string.isRequired
  }

  state = {
    data: undefined,
    editAlias: undefined,
  }

  DETAIL_URL = window.easyThumbnailAdminOptions.api.detail
  SET_OPTION_URL = window.easyThumbnailAdminOptions.api['set-option']
  DELETE_OPTION_URL = window.easyThumbnailAdminOptions.api['delete-option']

  componentDidMount () {
    this.fetchData()
  }

  fetchData () {
    $.ajax({
      url: this.DETAIL_URL,
      data: this.props
    })
      .then((data) => {
        this.setState({data})
      })
  }

  onClickEditHandler = ({alias}) => {
    this.setState({editAlias: alias})
  }
  onSaveOptionHandler = ({data, alias}) => {
    console.log(data, alias)
    $.ajax({
      url: this.SET_OPTION_URL,
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({...this.props, alias, options: data})
    })
      .then((data) => {
        this.setState({editAlias: false})
        this.fetchData()
      })
  }

  onResetOptionHandler = ({alias}) => {
    $.ajax({
      url: this.DELETE_OPTION_URL,
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({...this.props, alias})
    })
      .then((data) => {
        this.setState({editAlias: false})
        this.fetchData()
      })
  }

  render () {
    const {data, editAlias} = this.state
    if (!data) {
      return (
        <div>
          Loading...
        </div>
      )
    }
    if (editAlias) {
      const {url, thumbnails} = data
      return <EditThumbnail url={url}
                            thumbnail={thumbnails[editAlias]}
                            onCancel={() => this.setState({editAlias: null})}
                            onSave={(data) => {
                              this.onSaveOptionHandler({data, alias: editAlias})
                            }}
      />
    }

    return <InfoDisplay data={data}
                        onClickEdit={this.onClickEditHandler}
                        onClickReset={this.onResetOptionHandler}
    />
  }
}