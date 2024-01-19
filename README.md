# CV

## How to set up Jekyll on MacOS
https://jekyllrb.com/docs/installation/macos/
- `brew install chruby ruby-install xz`
- `ruby-install ruby 3.1.3`
- `echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc`
- `echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc`
- `echo "chruby ruby-3.1.3" >> ~/.zshrc # run 'chruby' to see actual version`
- `gem install jekyll`
