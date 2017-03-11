function distance(s1::AbstractString, s2::AbstractString)

  if length(s1) != length(s2)
    throw(ArgumentError("Provided strings are not of equal length"))
  else
    diffCount = 0
    for i in 1:endof(s1)
      if s1[i] != s2[i]
        diffCount += 1
      end
    end
    return(diffCount)
  end
end
