test:
	python -m unittest discover -s tests -v

smoke:
	python -m simulator --scenario retry-storm --messages 1000 --failure-rate 0.05
