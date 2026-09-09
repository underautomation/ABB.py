from enum import IntEnum

class MastershipDomain(IntEnum):
	'''Domain of the controller a client can take the mastership of. Mastership is what a client has to hold before it is allowed to change anything in a domain. Only one client at a time holds it, and it stays held until the client releases it or its connection ends.The two connection versions do not cut the controller in the same domains: a connection established with version 1 keeps the configuration and the RAPID programs apart, a connection established with version 2 covers both with . Whichever name is used, the service asks the connected controller for the domains it really has.'''
	Edit = 0 # Everything that changes the system itself: its configuration and its RAPID programs. On a connection established with version 1, where the two are separate domains, asking for this one takes and together.
	Motion = 1 # The movement of the robot: jogging, the mechanical units and everything that makes an axis move
	Configuration = 2 # The system parameters of the controller. On a connection established with version 2, where it is not a domain of its own, this is the same domain as .
	Rapid = 3 # The RAPID programs and their data. On a connection established with version 2, where it is not a domain of its own, this is the same domain as .
