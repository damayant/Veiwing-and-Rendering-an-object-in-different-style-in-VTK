import vtk


filename = 'teapot.stl'

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

#Computation of normals
normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(reader.GetOutputPort())

# Set object properties
prop = actor.GetProperty()
prop.SetInterpolationToPhong() # Set shading to Phong
prop.ShadingOn()
prop.SetDiffuse(0.8) # 0.8
prop.SetAmbient(0.3) # 0.3
prop.SetSpecular(1.0) # 1.0


# Define light
light = vtk.vtkLight ()
light.SetLightTypeToSceneLight()
light.SetAmbientColor(1, 1, 1)
light.SetDiffuseColor(1, 1, 1)
light.SetSpecularColor(1, 1, 1)
light.SetPosition(-100, 100, 25)
light.SetFocalPoint(0,0,0)
light.SetIntensity(0.8)



# Create a rendering window and renderer
ren = vtk.vtkRenderer()
# Add the light to the renderer
ren.AddLight(light)
 
# Assign actor to the renderer
ren.AddActor(actor)

##################

reader2 = vtk.vtkSTLReader()
reader2.SetFileName(filename)

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)

#Computation of normals
normals2 = vtk.vtkPolyDataNormals()
normals2.SetInputConnection(reader2.GetOutputPort())

# Set object properties
prop2 = actor2.GetProperty()
prop2.SetInterpolationToFlat() # Set shading to Flat
prop2.ShadingOn()
prop2.SetDiffuse(0.8) # 0.8
prop2.SetAmbient(0.3) # 0.3
prop2.SetSpecular(1.0) # 1.0


# Define light
light2 = vtk.vtkLight ()
light2.SetLightTypeToSceneLight()
light2.SetAmbientColor(1, 1, 1)
light2.SetDiffuseColor(1, 1, 1)
light2.SetSpecularColor(1, 1, 1)
light2.SetPosition(-100, 100, 25)
light2.SetFocalPoint(0,0,0)
light2.SetIntensity(0.8)

# Create a rendering window and renderer
ren2 = vtk.vtkRenderer()
# Add the light to the renderer
ren2.AddLight(light2)
# Assign actor to the renderer
ren2.AddActor(actor2)

#########################################
 

reader3 = vtk.vtkSTLReader()
reader3.SetFileName(filename)

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(reader.GetOutputPort())

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)

#Computation of normals
normals3 = vtk.vtkPolyDataNormals()
normals3.SetInputConnection(reader.GetOutputPort())

# Set object properties
prop3 = actor3.GetProperty()
prop3.SetRepresentationToWireframe() #to get the representation in WireFramework

# Create a rendering window and renderer
ren3 = vtk.vtkRenderer()

# Assign actor to the renderer
ren3.AddActor(actor3)


##############################################################


reader4 = vtk.vtkSTLReader()
reader4.SetFileName(filename)
mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputConnection(reader2.GetOutputPort())

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)

#Computation of normals
normals4 = vtk.vtkPolyDataNormals()
normals4.SetInputConnection(reader4.GetOutputPort())

# Set object properties
prop4 = actor4.GetProperty()
prop4.ShadingOn()
prop4.SetRepresentationToPoints() #Set the representation to points 


# Create a rendering window and renderer
ren4 = vtk.vtkRenderer()

# Assign actor to the renderer
ren4.AddActor(actor4)





ren.SetViewport(0,0,0.5,0.5)  #Flat Shading (PORT 1)
ren4.SetViewport(0.5,0.5,1,1) #Point Representation (PORT 2)
ren2.SetViewport(0,0.5,0.5,1) #Phong Shading (PORT 3)
ren3.SetViewport(0.5,0,1,0.5) #Wireframe representation (PORT 4)



renWin = vtk.vtkRenderWindow()

renWin.AddRenderer(ren)
renWin.AddRenderer(ren2)
renWin.AddRenderer(ren3)
renWin.AddRenderer(ren4)
renWin.Render()
# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#converting to jpeg file format
w2if = vtk.vtkWindowToImageFilter()
w2if.SetInput(renWin)
w2if.Update()
 
writer = vtk.vtkJPEGWriter()
writer.SetFileName("assignment1.jpeg")
writer.SetInputConnection(w2if.GetOutputPort())
writer.Write()



# Enable user interface interactor
iren.Initialize()
#renWin.Render()
iren.Start()
