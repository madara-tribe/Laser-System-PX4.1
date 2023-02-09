import os
import yaml
    
def hw_main(opt):
    with open(opt.hyp, errors='ignore') as f:
        hyp = yaml.safe_load(f)
    if opt.plot:
        from JetsonNano.Controller import plot
        plot.run_cameras(hyp)
    elif opt.mov:
        from JetsonNano.Controller import movie
        movie.run_cameras(hyp)
    elif opt.pwm:
        from JetsonNano.Controller import pwm
        pwm.run_cameras(opt, hyp)
    #else:
    #    tmpdir = "/tmp/tmp_2s487t8" #str(sys.argv[2])
     #   os.system("python3 JetsonNano/pwm/dual_pwm.py")
    
