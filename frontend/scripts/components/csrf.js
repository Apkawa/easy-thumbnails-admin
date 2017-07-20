'use strict'
import $ from 'jquery'

// using jQuery
function getCookie (name) {
  var cookieValue = null
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';')
    for (var i = 0; i < cookies.length; i++) {
      var cookie = $.trim(cookies[i])
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}
function csrfSafeMethod (method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

export default function csrfSetup ({cookieName = 'csrftoken', headerName = 'X-CSRFToken'} = {}) {
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      const csrftoken = getCookie(cookieName)
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader(headerName, csrftoken)
      }
    }
  })
}