#!/usr/bin/env python
# coding: utf-8
import pikepdf

pdf = pikepdf.open(input("Enter the filename/location: "))
pdf.save('EditingEnabled.pdf')





