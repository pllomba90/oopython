"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self,start=0):
        """Initial creation of a serial number starting at 0 unless otherwise indicated."""
        self.start = self.next = start

    def __repr__ (self):
        """Creates a representation of the class"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """Method to actually make a serial number"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets our generator."""
        self.next = self.start
