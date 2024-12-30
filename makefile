run: src/standard_test.py
	python3 src/standard_test.py

clean: 
	rm -r src/__pycache__

format: src/*.py
	black src/*.py