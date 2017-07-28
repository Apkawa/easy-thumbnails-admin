'use strict'
import React, { Component } from 'react'
import PropTypes from 'prop-types'

import style from './style.scss?module'
import AliasItem from './AliasItem'

export default function InfoDisplay ({data, onClickEdit = () => {}, onClickReset = () => {}}) {
  const {name, url, thumbnails} = data
  return (
    <div className={style.container}>
      <div className={style.original}>
        <h2>Original</h2>
        <div>
          <img src={url} alt={name}/>
        </div>
      </div>
      <hr/>
      <h2>Aliases</h2>
      <div className={style.aliasList}>
        {Object.entries(thumbnails).map(
          ([alias, thumb]) => <AliasItem
            alias={alias}
            thumbnailData={thumb}
            onClickEdit={onClickEdit}
            onClickReset={onClickReset}
          />)}
      </div>
    </div>
  )
}