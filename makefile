# A very simple makefile example that produces log files and zips them

codestyle.log: ./demo/*.py
	@echo "Running tests..."
	@flake8 ./demo > codestyle.log
	@cat codestyle.log
	@echo "Done!"

test.log: ./demo/*.py
	@echo "Running tests..."
	@pytest -v ./demo > test.log
	@cat test.log
	@echo "Done!"

logs.zip: test.log codestyle.log
	@zip logs.zip ./*.log

clean:
	@rm ./*.log