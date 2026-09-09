from __future__ import annotations
import typing
from underautomation.abb.rws.data.directory_listing import DirectoryListing
from UnderAutomation.ABB.Rws.Services import FileService as file_service

class FileService:
	'''File Service - Provides access to the robot controller file system Compatibility:Version 1: directory operations with basic functionalityVersion 2: extended file operations'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_service()
		else:
			self._instance = _internal

	def list_directory(self, path: str) -> DirectoryListing:
		'''Lists contents of a directory resource (synchronous) Environment variables (e.g. $home, $temp) and devices are treated as directories.When listing the root path ("/", null, or "\\"), the response includes available devices in .The complete content is always returned, however many entries the directory holds.

		:param path: Path to the directory (e.g. "$home", "$home/mydir", "hd0a:/data"), or null/"/"/"\\" for root
		:returns: Directory listing containing files, subdirectories, and devices
		'''
		return DirectoryListing(None, self._instance.ListDirectory(path))

	def delete_directory(self, path: str) -> None:
		'''Deletes a directory and all its subdirectories and files (synchronous)

		:param path: Path to the directory to delete (e.g. "$home/testdir")
		'''
		self._instance.DeleteDirectory(path)

	def create_directory(self, path: str, newName: str) -> None:
		'''Creates a new directory (synchronous) The newName parameter can contain nested directory structure (e.g. "parentdir/subdir")which will create both directories if they don't exist.

		:param path: Parent directory path (e.g. "$home", "$home/existing")
		:param newName: Name of the new directory (can be nested: "dir1/dir2")
		'''
		self._instance.CreateDirectory(path, newName)

	def rename_directory(self, path: str, newName: str) -> None:
		'''Renames a directory (synchronous)

		:param path: Path to the directory to rename (e.g. "$home/dir1")
		:param newName: New directory name (relative or absolute depending on controller behavior)
		'''
		self._instance.RenameDirectory(path, newName)

	def copy_directory(self, path: str, newName: str, overwrite: bool) -> None:
		'''Copies a directory (synchronous)

		:param path: Path to the directory to copy (e.g. "$home/dir1")
		:param newName: New directory name (relative or absolute)
		:param overwrite: Whether to overwrite if target exists
		'''
		self._instance.CopyDirectory(path, newName, overwrite)

	def delete_file(self, path: str) -> None:
		'''Deletes a file (synchronous)

		:param path: Path to the file to delete (e.g. "$home/file.txt")
		'''
		self._instance.DeleteFile(path)

	def rename_file(self, path: str, newName: str) -> None:
		'''Renames a file (synchronous)

		:param path: Path to the file to rename (e.g. "$home/file.txt")
		:param newName: New file name
		'''
		self._instance.RenameFile(path, newName)

	def copy_file(self, path: str, newName: str, overwrite: bool) -> None:
		'''Copies a file (synchronous)

		:param path: Path to the file to copy (e.g. "$home/file.txt")
		:param newName: New file name (relative or absolute)
		:param overwrite: Whether to overwrite if target exists
		'''
		self._instance.CopyFile(path, newName, overwrite)

	def get_file_as_bytes(self, path: str) -> typing.List[int]:
		'''Gets file content as raw bytes (synchronous)

		:param path: Path to the file (e.g. "$home/file.txt")
		:returns: File content as byte array
		'''
		return self._instance.GetFileAsBytes(path)

	def get_file_to_destination(self, path: str, localPath: str) -> None:
		'''Downloads a file to a local path (synchronous)

		:param path: Path to the file (e.g. "$home/file.txt")
		:param localPath: Local file path to write
		'''
		self._instance.GetFileToDestination(path, localPath)

	def upload_file_from_bytes(self, path: str, content: typing.List[int], contentType: str=None) -> None:
		'''Uploads a file from raw bytes (synchronous)

		:param path: Path to the file (e.g. "$home/file.txt")
		:param content: Raw file content
		:param contentType: Content type (default: application/octet-stream)
		'''
		self._instance.UploadFileFromBytes(path, content, contentType)

	def upload_file_from_path(self, path: str, localPath: str, contentType: str=None) -> None:
		'''Uploads a local file to the controller (synchronous)

		:param path: Target file path on controller (e.g. "$home/file.txt")
		:param localPath: Local file path to upload
		:param contentType: Content type (default: application/octet-stream)
		'''
		self._instance.UploadFileFromPath(path, localPath, contentType)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
