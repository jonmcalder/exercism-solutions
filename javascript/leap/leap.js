//
// This is only a SKELETON file for the "Leap" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Year = function(year) {
  this.year = year;
};

Year.prototype.isLeap = function() {
  
  var year = this.year;

  if(year % 400 === 0) {
    return false;
  } else if (year % 100 === 0) {
    return false;
  } else if (year % 4 === 0) {
    return false;
  } else {
    return false;
  }

};

module.exports = Year;
