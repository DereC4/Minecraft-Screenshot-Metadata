import re, shutil, subprocess, argparse
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor as TPE

p=re.compile(r'^(\d{4})-(\d{2})-(\d{2})_(\d{2})\.(\d{2})\.(\d{2})(?:\.(png|jpg|jpeg))?$')
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('-i','--input',type=Path,default=Path('input'))
    ap.add_argument('-o','--output',type=Path,default=Path('output'))
    ap.add_argument('--dry-run',action='store_true')
    ap.add_argument('-w','--workers',type=int,default=8)
    a=ap.parse_args()
    a.input.mkdir(parents=True,exist_ok=True); a.output.mkdir(parents=True,exist_ok=True)
    cmds=[]
    for f in sorted([x for x in a.input.iterdir() if x.is_file() and not x.name.startswith('.')]):
        m=p.match(f.name)
        if not m: continue
        y,mo,d,h,mi,s,_=m.groups()
        dt=datetime(int(y),int(mo),int(d),int(h),int(mi),int(s),tzinfo=timezone.utc)
        exif=dt.strftime('%Y:%m:%d %H:%M:%S'); xmp=dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        t=a.output/f.name; shutil.copy2(f,t)
        cmd=['exiftool','-overwrite_original',f'-AllDates={exif}',f'-xmp:CreateDate={xmp}',f'-xmp:ModifyDate={xmp}',f'-xmp:MetadataDate={xmp}',f'-PNG:CreationTime={xmp}',str(t)]
        (print(' '.join(cmd)) if a.dry_run else cmds.append(cmd))
    (None if a.dry_run else (lambda: [*TPE(max_workers=a.workers).map(subprocess.run,cmds)])())
