'use strict'
import React, { Component } from 'react'
import PropTypes from 'prop-types'

import style from './style.scss?module'

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
          ([alias, thumb]) =>
            <div className={style.aliasItem}>
              <img src={`${thumb.url}?r=${new Date().getTime()}`} alt={thumb.name}/>
              <h3>{alias}</h3>
              <button onClick={() => onClickEdit({alias, thumb}) }>Edit</button>
              {thumb.options.thumbnail_option_id
                ? <button onClick={() => onClickReset({alias, thumb}) }>Reset</button>
                : null}
            </div>
        )}
      </div>
    </div>
  )
}