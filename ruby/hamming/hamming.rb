class Hamming
  def self.compute(strandA, strandB)
    if strandA.length == strandB.length
      @hamming = 0
      strandA.split("").zip(strandB.split("")) do |a, b|
        if a != b
          @hamming += 1
        end
      end
      return @hamming
    else
      raise(ArgumentError)
    end
  end
end