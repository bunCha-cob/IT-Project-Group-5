import subprocess
import sys
with open('test.log', 'wb') as f:  
    process = subprocess.Popen("import sys; print(Hello from other console)", stdout=subprocess.PIPE)
    for line in iter(process.stdout.readline, 'b'):  
        sys.stdout.write(line)
        f.write(line)