'use strict'

import superagent from 'superagent'
import 'superagent-django-csrf'

export const API = {
  get DETAIL_URL () {
    return window.easyThumbnailAdminOptions.api.detail
  },

  get SET_OPTION_URL () {
    return window.easyThumbnailAdminOptions.api['set-option']

  },
  get DELETE_OPTION_URL () {
    return window.easyThumbnailAdminOptions.api['delete-option']
  }
}

export class Client {

  _build_client (method, path) {
    return superagent[method](path)
      .withCredentials()
      .set('Content-Type', 'application/json')
  }

  detail ({name, target}) {
    return this._build_client('get', API.DETAIL_URL)
      .query({name, target})
  }

  setOption ({name, target, alias, options}) {
    return this._build_client('post', API.SET_OPTION_URL)
      .send({name, target, alias, options})
  }

  deleteOption ({name, target, alias}) {
    return this._build_client('post', API.DELETE_OPTION_URL)
      .send({name, target, alias})

  }

}

export default new Client()