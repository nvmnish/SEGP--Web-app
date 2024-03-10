from django.shortcuts import render

def client_side_landing(request):
    return render(request, 'cancerAnalysis/ClientSideLanding.html')
def virtual_staining(request):
    return render(request, 'cancerAnalysis/virtual-staining.html')
def spatial_features(request):
    return render(request, 'cancerAnalysis/spatial-features.html')