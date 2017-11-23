'use strict'
import React from 'react'

import style from './style.scss?module'

function Size (size) {
  if (size) {
    const [width, height] = size
    return (
      <div>
        Size: {width}x{height}px
      </div>
    )
  }
  return 'Size: original'

}

export default function AliasItem ({
                                     alias,
                                     thumbnailData,
                                     onClickEdit,
                                     onClickReset
                                   }) {
  const {url, name, admin = {}, options: {thumbnail_option_id, ...options}} = thumbnailData
  const thumb = thumbnailData
  const {size} = options

  return (<div className={style.aliasItem}>
      <div className={style.aliasItemImage}>
        <img src={`${url}?r=${new Date().getTime()}`} alt={name}/>
      </div>
      <div>
        <h3>{alias}</h3>
        <div>
          {(admin && admin.help_text) || null}
        </div>
        {Size(size)}
        <button onClick={() => onClickEdit({alias, thumb})}>Edit</button>
        {thumbnail_option_id
          ? <button onClick={() => onClickReset({alias, thumb})}>Reset</button>
          : null}
      </div>
    </div>
  )

}
