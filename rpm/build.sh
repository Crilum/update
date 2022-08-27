#!/usr/bin/env bash

# This script will package the `update` script into a `rpm` package.

declare -r NAME="update"
declare -r BUILD_DIR="$(pwd)"
declare -r VERSION="$(grep "version=" "${BUILD_DIR}/${NAME}" | cut -d"\"" -f2 | cut -d"v" -f2)"

echo "name: $NAME, build dir: $BUILD_DIR, version: $version"

if command -v dnf &>/dev/null; then
   command -v rpmdev-setuptree &> /dev/null && command -v rpmbuild &>/dev/null || sudo dnf install rpm-build rpmdevtools -y
elif command -v yum &>/dev/null; then
   command -v rpmdev-setuptree &> /dev/null && command -v rpmbuild &>/dev/null || sudo yum install rpm-build rpmdevtools -y
elif command -v apt &>/dev/null; then
   command -v rpmbuild &>/dev/null || sudo apt install rpm -y
else
   printf 'No suitable package manager found!! Exiting...'
   exit 1
fi

# Exit out when running the script as root.
if [[ ${UID} -eq 0 ]]; then
   printf 'Please run this script as a normal user.'
   exit 1
fi

# Create the necessary directories.
mkdir -p "${HOME}/rpmbuild/"{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p "${HOME}/rpmbuild/BUILD/${NAME}-${VERSION}"
mkdir -p "${BUILD_DIR}/${NAME}-${VERSION}"

# Create the tarball.
echo "Creating tarball..."
cp -r "${BUILD_DIR}/${NAME}" "${BUILD_DIR}/${NAME}-${VERSION}"
echo "Linking update to up..."
ln -v -s /usr/bin/update "${BUILD_DIR}/${NAME}-${VERSION}/up" || echo "failed to link update to up!"
echo "Done!"
tar --create --file "${NAME}-${VERSION}.tar.gz" "${NAME}-${VERSION}"

# Move the tarball to the SOURCES directory.
mv "${BUILD_DIR}/${NAME}-${VERSION}.tar.gz" "${HOME}/rpmbuild/SOURCES/"

# Update the version number.
sed -i "s/VERSION THE SCRIPT WILL UPDATE THIS!/${VERSION}/g" "${BUILD_DIR}/rpm/${NAME}.spec"

# Copy over the spec file.
cp -r "${BUILD_DIR}/rpm/${NAME}.spec" "${HOME}/rpmbuild/SPECS/${NAME}.spec"

# build RPM package.
rpmbuild -ba "${HOME}/rpmbuild/SPECS/${NAME}.spec"

# Cleanup
rm -rf "${NAME}-${VERSION}"

