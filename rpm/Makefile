
GIT_COMMIT ?= HEAD
GIT_VERSION := $(shell git describe $(GIT_COMMIT) 2>/dev/null)
GIT_VERSION := $(subst -, ,$(GIT_VERSION))

VERSION ?= $(word 1,$(GIT_VERSION))
ifeq (,$(VERSION))
VERSION := 0.1
endif
RELEASE ?= $(word 2,$(GIT_VERSION)).$(word 3,$(GIT_VERSION))
ifeq (.,$(RELEASE))
RELEASE := 0
endif

SOURCE_TARGET := rpmbuild/SOURCES/monit-remote-$(VERSION).tar.gz
SOURCE ?= $(SOURCE_TARGET)

.PHONY: all version clean mkdir prepare_source  rpm

all: rpm

version:
	@if [ "$(origin VERSION)" = "file" -a -z "$(GIT_VERSION)" ] ; then \
	    echo >&2 WARNING: Unable to determine version via git describe; \
	    sleep 1; \
	fi
	@echo Version $(VERSION)-$(RELEASE); \

clean:
	rm -rf rpmbuild

mkdir: clean
	mkdir -p rpmbuild
	mkdir -p rpmbuild/BUILD
	mkdir -p rpmbuild/BUILDROOT
	mkdir -p rpmbuild/RPMS
	mkdir -p rpmbuild/SOURCES
	mkdir -p rpmbuild/SRPMS

$(SOURCE_TARGET): mkdir
	if [ -f "$(SOURCE)" ]; then \
		cp $(SOURCE) $(SOURCE_TARGET); \
	else \
		(cd `git rev-parse --show-toplevel` && git archive --format=tar \
		        --prefix=monit-release-$(VERSION)/ $(GIT_COMMIT)) | gzip > $@; \
	fi

rpm: version $(SOURCE_TARGET)
	rpmbuild $(RPM_OPTS) \
	  --define "_topdir %(pwd)" \
	  --define "_builddir %{_topdir}/rpmbuild/BUILD" \
	  --define "_buildrootdir %{_topdir}/rpmbuild/BUILDROOT" \
	  --define "_rpmdir %{_topdir}/rpmbuild/RPMS" \
	  --define "_srcrpmdir %{_topdir}/rpmbuild/SRPMS" \
	  --define "_specdir %{_topdir}" \
	  --define "_sourcedir  %{_topdir}/rpmbuild/SOURCES" \
	  --define "VERSION $(VERSION)" \
	  --define "RELEASE $(RELEASE)" \
	  -ba monit-remote.spec
