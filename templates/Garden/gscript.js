var body = document.body;
var content = document.querySelector('.js-content');
var blocks = document.querySelectorAll('.block');

var updateOffset = function updateOffset() {
  requestAnimationFrame(updateOffset);
  body.style.setProperty('--y', content.scrollTop);
  updateProps();
};

var updateProps = function updateProps() {
  var i = -1;
  var _iteratorNormalCompletion = true;
  var _didIteratorError = false;
  var _iteratorError = undefined;

  try {
    for (var _iterator = blocks[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
      var block = _step.value;

      i += 1;
      var top = blocks[i].getBoundingClientRect().top;
      if (top < window.innerHeight * 1.3 && top > window.innerHeight * -1.3) {
        body.style.setProperty('--yBlock-' + (i + 1), top);
      } else {
        body.style.setProperty('--yBlock-' + (i + 1), 0);
      }
    }
  } catch (err) {
    _didIteratorError = true;
    _iteratorError = err;
  } finally {
    try {
      if (!_iteratorNormalCompletion && _iterator.return) {
        _iterator.return();
      }
    } finally {
      if (_didIteratorError) {
        throw _iteratorError;
      }
    }
  }
};

updateProps();
updateOffset();