# Copyright (c) 2025, Serra ICT and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase

from .process_segment import ProcessSegment

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestProcessSegment(UnitTestCase):
	"""
	Unit tests for ProcessSegment.
	Use this class for testing individual functions and methods.
	"""

	def test_equality(self):
		"""Test equality of ProcessSegment instances."""
		# Create two instances of ProcessSegment
		process_segment1 = frappe.get_doc({"doctype": "Process Segment", "name": "Test Segment 1"})
		process_segment2 = frappe.get_doc({"doctype": "Process Segment", "name": "Test Segment 2"})
		process_segment1b = frappe.get_doc({"doctype": "Process Segment", "name": "Test Segment 1"})

		# Check if they are equal
		self.assertEqual(process_segment1, process_segment1)
		self.assertEqual(process_segment2, process_segment2)
		self.assertNotEqual(process_segment1, process_segment2)
		self.assertNotEqual(process_segment1, process_segment1b)

	def test_controller(self):
		"""Test controller of ProcessSegment."""
		# This is loaded from the database actually:
		doc = frappe.get_doc({"doctype": "Process Segment", "name": "Oppotten"})
		self.assertIsNotNone(doc)
		ps = ProcessSegment(doc)
		self.assertIsNotNone(ps)
		print(ps.name)
		print(ps.doctype)
		print(ps)


class IntegrationTestProcessSegment(IntegrationTestCase):
	"""
	Integration tests for ProcessSegment.
	Use this class for testing interactions between multiple components.
	"""

	pass
