from lilaclib import *

build_prefix = 'extra-x86_64'
depends = [
  ('rust-nightly', 'rust-std-nightly-x86_64-unknown-linux-gnu'),
  ('rust-nightly', 'rust-nightly'),
  ('rust-nightly', 'cargo-nightly'),
]

def pre_build():
  # TODO: rebuild trigger by rust-nightly
  if _G.oldver == _G.newver:
    for line in edit_file('PKGBUILD'):
      if line.startswith('pkgrel='):
        rel = int(line.split('=', 1)[1]) + 1
        line = 'pkgrel=%s' % rel
      print(line)
  else:
    for line in edit_file('PKGBUILD'):
      if line.startswith('pkgver='):
        line = 'pkgver=%s' % _G.newver
      elif line.startswith('pkgrel='):
        line = 'pkgrel=1'
      print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
