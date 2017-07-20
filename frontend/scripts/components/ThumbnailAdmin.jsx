'use strict'
import React, { Component } from 'react'
import PropTypes from 'prop-types'

import Modal from 'react-modal'

import Info from './Info'

const customStyles = {
  content: {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)'
  }
}

export default class ThumbnailAdmin extends Component {
  static propTypes = {
    name: PropTypes.string.isRequired,
    target: PropTypes.string.isRequired
  }

  state = {
    open: true,
  }

  closeModal = () => {
    this.setState({open: false})
  }

  render () {
    return (
      <div>
        <Modal
          isOpen={this.state.open}
          onAfterOpen={this.afterOpenModal}
          onRequestClose={this.closeModal}
          style={customStyles}
          contentLabel="Example Modal"
        >
          <Info {...this.props}/>
        </Modal>
      </div>
    )
  }
}