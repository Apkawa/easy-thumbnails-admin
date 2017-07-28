'use strict'
import React, { Component } from 'react'
import PropTypes from 'prop-types'

import client from '../api'

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

  componentDidMount () {
    this.fetchData()
  }

  fetchData () {
    client.detail(this.props).then(({body}) => {
      this.setState({data: body})
    })
  }

  onClickEditHandler = ({alias}) => {
    this.setState({editAlias: alias})
  }

  onSaveOptionHandler = ({data, alias}) => {
    client.setOption({
      ...this.props,
      alias,
      options: data
    }).then(() => {
      this.setState({editAlias: false})
      this.fetchData()
    })
  }

  onResetOptionHandler = ({alias}) => {
    client.deleteOption({
      ...this.props,
      alias,
    })
      .then(() => {
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