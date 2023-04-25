cdef class iris:
	cdef public:
		unsigned long int number
		bint key
	def __cinit__(self, key, number) -> None:
		self.key	= key
		self.number = number 

	cpdef tuple  iris(self) : 
		if   self.key is False : return (None, None)
		else:
			if self.number % 2 == 0 : return (self.key, True)
			else : return (self.key, False)

	cdef str setosa(self):
		return f"{self.key}, {self.number}" 
