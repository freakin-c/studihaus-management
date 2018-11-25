# StudiHaus Management

This Django project aims to be a simple management tool for halls of residence.
It allows setting up the rooms and associating them with the residents.

# Getting Started

**Prepare project**

```{bash}
# install mariadb server with your favourite package manager
# and start the service with your systems init system or others
pacman -S mariadb
systemctl start mariadb.service

# install python dependencies inside of virtual environment
python -m venv studihaus-venv
source studihaus-venv/bin/activate
pip install mysqlclient django
git clone https://github.com/freakin-c/studihaus-management.git
```

**Rename** `settings.py.default` to `settings.py` and **apply changes** as stated inside it.

**Run server** with `python studihaus-management/manage.py runserver`.
Remeber to have *mariadb* or other running.

# Milestones

1. Create user interface (views) apart from admin site.
2. History of tenancies per resident/room.
3. Uploading of template documents in `.odt` format for rendering for (selected) residents (e.g. create new leases).
4. Checklist for supervising the rent payment.
