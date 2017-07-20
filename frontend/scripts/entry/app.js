'use strict'
import $ from 'jquery'
import React from 'react'
import { render, unmountComponentAtNode } from  'react-dom'
import { ThumbnailAdmin } from '../components'

$(() => {
  const $container = $(`<div id="easy-thumbnail-container"/>`)
  $('body').append($container)
  const container = $container[0]

  $('[data-easy-thumbnail-admin-input]').each(function (index) {
    const $el = $(this)
    const data = $el.data()
    $el.siblings('a').on('click', (e) => {
      e.preventDefault()
      unmountComponentAtNode(container)
      render(
        <ThumbnailAdmin {...data}/>,
        container
      )
      return false
    })
  })

})