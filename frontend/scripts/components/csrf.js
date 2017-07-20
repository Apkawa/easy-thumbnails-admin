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
  if ($.prototype.__csrf_patched || XMLHttpRequest.prototype._csrf) {
    return
  }
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if ($.prototype.__csrf_patched || XMLHttpRequest.prototype._csrf) {
        return
      }
      const csrftoken = getCookie(cookieName)
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        console.log(headerName, csrftoken)
        xhr.setRequestHeader(headerName, csrftoken)
        $.prototype.__csrf_patched = csrftoken
        XMLHttpRequest.prototype._csrf = csrftoken
      }
    }
  })
}