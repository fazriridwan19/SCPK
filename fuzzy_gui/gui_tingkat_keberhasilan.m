function varargout = gui_tingkat_keberhasilan(varargin)
% GUI_TINGKAT_KEBERHASILAN MATLAB code for gui_tingkat_keberhasilan.fig
%      GUI_TINGKAT_KEBERHASILAN, by itself, creates a new GUI_TINGKAT_KEBERHASILAN or raises the existing
%      singleton*.
%
%      H = GUI_TINGKAT_KEBERHASILAN returns the handle to a new GUI_TINGKAT_KEBERHASILAN or the handle to
%      the existing singleton*.
%
%      GUI_TINGKAT_KEBERHASILAN('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUI_TINGKAT_KEBERHASILAN.M with the given input arguments.
%
%      GUI_TINGKAT_KEBERHASILAN('Property','Value',...) creates a new GUI_TINGKAT_KEBERHASILAN or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before gui_tingkat_keberhasilan_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to gui_tingkat_keberhasilan_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help gui_tingkat_keberhasilan

% Last Modified by GUIDE v2.5 21-Apr-2021 12:01:07

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @gui_tingkat_keberhasilan_OpeningFcn, ...
                   'gui_OutputFcn',  @gui_tingkat_keberhasilan_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before gui_tingkat_keberhasilan is made visible.
function gui_tingkat_keberhasilan_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output_tingkat args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to gui_tingkat_keberhasilan (see VARARGIN)

% Choose default command line output_tingkat for gui_tingkat_keberhasilan
handles.output_tingkat = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes gui_tingkat_keberhasilan wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = gui_tingkat_keberhasilan_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output_tingkat args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output_tingkat from handles structure
varargout{1} = handles.output_tingkat;


% --- Executes on button press in btn_exit.
function btn_exit_Callback(hObject, eventdata, handles)
% hObject    handle to btn_exit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
close



function output_tingkat_Callback(hObject, eventdata, handles)
% hObject    handle to output_tingkat (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of output_tingkat as text
%        str2double(get(hObject,'String')) returns contents of output_tingkat as a double


% --- Executes during object creation, after setting all properties.
function output_tingkat_CreateFcn(hObject, eventdata, handles)
% hObject    handle to output_tingkat (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function value_dosen_Callback(hObject, eventdata, handles)
% hObject    handle to value_dosen (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of value_dosen as text
%        str2double(get(hObject,'String')) returns contents of value_dosen as a double
v_dosen = str2double(get(hObject,'string'));
handles.v_dosen = v_dosen;
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function value_dosen_CreateFcn(hObject, eventdata, handles)
% hObject    handle to value_dosen (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function value_nilai_Callback(hObject, eventdata, handles)
% hObject    handle to value_nilai (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of value_nilai as text
%        str2double(get(hObject,'String')) returns contents of value_nilai as a double
v_nilai = str2double(get(hObject,'string'));
handles.v_nilai = v_nilai;
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function value_nilai_CreateFcn(hObject, eventdata, handles)
% hObject    handle to value_nilai (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in btn_proc.
function btn_proc_Callback(hObject, eventdata, handles)
% hObject    handle to btn_proc (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
a = readfis('tingkat_keberhasilan');
out = evalfis(a, [handles.v_dosen handles.v_nilai]);
set(handles.output, 'string', out);



function output_Callback(hObject, eventdata, handles)
% hObject    handle to output (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of output as text
%        str2double(get(hObject,'String')) returns contents of output as a double


% --- Executes during object creation, after setting all properties.
function output_CreateFcn(hObject, eventdata, handles)
% hObject    handle to output (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
