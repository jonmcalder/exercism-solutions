var DnaTranscriber = function() {};

rna_map = { "G":"`C", "C":"G", "T":"A", "A":"U" };

DnaTranscriber.prototype.toRna = function(dna) {

  var rna = "";

  for (var i = 0; i < dna.length; i++) {
    if (dna.charAt(i) in rna_map) {
      rna += rna_map[dna.charAt(i)];  
    }
    else {
      throw "Invalid input";
    }
  }

  return rna;

};

module.exports = DnaTranscriber;
