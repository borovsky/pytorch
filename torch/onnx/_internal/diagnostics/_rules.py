# mypy: allow-untyped-defs
"""
GENERATED CODE - DO NOT EDIT DIRECTLY
This file is generated by gen_diagnostics.py.
See tools/onnx/gen_diagnostics.py for more information.

Diagnostic rules for PyTorch ONNX export.
"""

import dataclasses
from typing import Tuple

# flake8: noqa
from torch.onnx._internal.diagnostics import infra


"""
GENERATED CODE - DO NOT EDIT DIRECTLY
The purpose of generating a class for each rule is to override the `format_message`
method to provide more details in the signature about the format arguments.
"""


class _NodeMissingOnnxShapeInference(infra.Rule):
    """Node is missing ONNX shape inference."""

    def format_message(self, op_name) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'The shape inference of {op_name} type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.'
        """
        return self.message_default_template.format(op_name=op_name)

    def format(  # type: ignore[override]
        self, level: infra.Level, op_name
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'The shape inference of {op_name} type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.'
        """
        return self, level, self.format_message(op_name=op_name)


class _MissingCustomSymbolicFunction(infra.Rule):
    """Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX."""

    def format_message(self, op_name) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'ONNX export failed on an operator with unrecognized namespace {op_name}. If you are trying to export a custom operator, make sure you registered it with the right domain and version.'
        """
        return self.message_default_template.format(op_name=op_name)

    def format(  # type: ignore[override]
        self, level: infra.Level, op_name
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ONNX export failed on an operator with unrecognized namespace {op_name}. If you are trying to export a custom operator, make sure you registered it with the right domain and version.'
        """
        return self, level, self.format_message(op_name=op_name)


class _MissingStandardSymbolicFunction(infra.Rule):
    """Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX."""

    def format_message(  # type: ignore[override]
        self, op_name, opset_version, issue_url
    ) -> str:
        """Returns the formatted default message of this Rule.

        Message template: "Exporting the operator '{op_name}' to ONNX opset version {opset_version} is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub: {issue_url}."
        """
        return self.message_default_template.format(
            op_name=op_name, opset_version=opset_version, issue_url=issue_url
        )

    def format(  # type: ignore[override]
        self, level: infra.Level, op_name, opset_version, issue_url
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "Exporting the operator '{op_name}' to ONNX opset version {opset_version} is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub: {issue_url}."
        """
        return (
            self,
            level,
            self.format_message(
                op_name=op_name, opset_version=opset_version, issue_url=issue_url
            ),
        )


class _OperatorSupportedInNewerOpsetVersion(infra.Rule):
    """Operator is supported in newer opset version."""

    def format_message(  # type: ignore[override]
        self, op_name, opset_version, supported_opset_version
    ) -> str:
        """Returns the formatted default message of this Rule.

        Message template: "Exporting the operator '{op_name}' to ONNX opset version {opset_version} is not supported. Support for this operator was added in version {supported_opset_version}, try exporting with this version."
        """
        return self.message_default_template.format(
            op_name=op_name,
            opset_version=opset_version,
            supported_opset_version=supported_opset_version,
        )

    def format(  # type: ignore[override]
        self, level: infra.Level, op_name, opset_version, supported_opset_version
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "Exporting the operator '{op_name}' to ONNX opset version {opset_version} is not supported. Support for this operator was added in version {supported_opset_version}, try exporting with this version."
        """
        return (
            self,
            level,
            self.format_message(
                op_name=op_name,
                opset_version=opset_version,
                supported_opset_version=supported_opset_version,
            ),
        )


class _FxGraphToOnnx(infra.Rule):
    """Transforms graph from FX IR to ONNX IR."""

    def format_message(self, graph_name) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'Transforming FX graph {graph_name} to ONNX graph.'
        """
        return self.message_default_template.format(graph_name=graph_name)

    def format(  # type: ignore[override]
        self, level: infra.Level, graph_name
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Transforming FX graph {graph_name} to ONNX graph.'
        """
        return self, level, self.format_message(graph_name=graph_name)


class _FxNodeToOnnx(infra.Rule):
    """Transforms an FX node to an ONNX node."""

    def format_message(self, node_repr) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'Transforming FX node {node_repr} to ONNX node.'
        """
        return self.message_default_template.format(node_repr=node_repr)

    def format(  # type: ignore[override]
        self, level: infra.Level, node_repr
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Transforming FX node {node_repr} to ONNX node.'
        """
        return self, level, self.format_message(node_repr=node_repr)


class _FxPass(infra.Rule):
    """FX graph transformation during ONNX export before converting from FX IR to ONNX IR."""

    def format_message(self, pass_name) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'Running {pass_name} pass.'
        """
        return self.message_default_template.format(pass_name=pass_name)

    def format(  # type: ignore[override]
        self, level: infra.Level, pass_name
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Running {pass_name} pass.'
        """
        return self, level, self.format_message(pass_name=pass_name)


class _NoSymbolicFunctionForCallFunction(infra.Rule):
    """Cannot find symbolic function to convert the "call_function" FX node to ONNX."""

    def format_message(self, target) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'No symbolic function to convert the "call_function" node {target} to ONNX. '
        """
        return self.message_default_template.format(target=target)

    def format(  # type: ignore[override]
        self, level: infra.Level, target
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'No symbolic function to convert the "call_function" node {target} to ONNX. '
        """
        return self, level, self.format_message(target=target)


class _UnsupportedFxNodeAnalysis(infra.Rule):
    """Result from FX graph analysis to reveal unsupported FX nodes."""

    def format_message(  # type: ignore[override]
        self, node_op_to_target_mapping
    ) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'Unsupported FX nodes: {node_op_to_target_mapping}. '
        """
        return self.message_default_template.format(
            node_op_to_target_mapping=node_op_to_target_mapping
        )

    def format(  # type: ignore[override]
        self, level: infra.Level, node_op_to_target_mapping
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Unsupported FX nodes: {node_op_to_target_mapping}. '
        """
        return (
            self,
            level,
            self.format_message(node_op_to_target_mapping=node_op_to_target_mapping),
        )


class _OpLevelDebugging(infra.Rule):
    """Report any op level validation failure in warnings."""

    def format_message(self, node, symbolic_fn) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'FX node: {node} and its onnx function: {symbolic_fn} fails on op level validation.'
        """
        return self.message_default_template.format(node=node, symbolic_fn=symbolic_fn)

    def format(  # type: ignore[override]
        self, level: infra.Level, node, symbolic_fn
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'FX node: {node} and its onnx function: {symbolic_fn} fails on op level validation.'
        """
        return self, level, self.format_message(node=node, symbolic_fn=symbolic_fn)


class _FindOpschemaMatchedSymbolicFunction(infra.Rule):
    """Find the OnnxFunction that matches the input/attribute dtypes by comparing them with their opschemas."""

    def format_message(self, symbolic_fn, node) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'The OnnxFunction: {symbolic_fn} is the nearest match of the node {node}.'
        """
        return self.message_default_template.format(symbolic_fn=symbolic_fn, node=node)

    def format(  # type: ignore[override]
        self, level: infra.Level, symbolic_fn, node
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'The OnnxFunction: {symbolic_fn} is the nearest match of the node {node}.'
        """
        return self, level, self.format_message(symbolic_fn=symbolic_fn, node=node)


class _FxNodeInsertTypePromotion(infra.Rule):
    """Determine if type promotion is required for the FX node. Insert cast nodes if needed."""

    def format_message(self, target) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'Performing explicit type promotion for node {target}. '
        """
        return self.message_default_template.format(target=target)

    def format(  # type: ignore[override]
        self, level: infra.Level, target
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Performing explicit type promotion for node {target}. '
        """
        return self, level, self.format_message(target=target)


class _FindOperatorOverloadsInOnnxRegistry(infra.Rule):
    """Find the list of OnnxFunction of the PyTorch operator in onnx registry."""

    def format_message(self, node) -> str:  # type: ignore[override]
        """Returns the formatted default message of this Rule.

        Message template: 'Checking if the FX node: {node} is supported in onnx registry.'
        """
        return self.message_default_template.format(node=node)

    def format(  # type: ignore[override]
        self, level: infra.Level, node
    ) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Checking if the FX node: {node} is supported in onnx registry.'
        """
        return self, level, self.format_message(node=node)


@dataclasses.dataclass
class _POERules(infra.RuleCollection):
    node_missing_onnx_shape_inference: _NodeMissingOnnxShapeInference = (
        dataclasses.field(
            default=_NodeMissingOnnxShapeInference.from_sarif(
                id="POE0001",
                name="node-missing-onnx-shape-inference",
                short_description={"text": "Node is missing ONNX shape inference."},
                full_description={
                    "text": "Node is missing ONNX shape inference. This usually happens when the node is not valid under standard ONNX operator spec.",
                    "markdown": "Node is missing ONNX shape inference.\nThis usually happens when the node is not valid under standard ONNX operator spec.\n",
                },
                message_strings={
                    "default": {
                        "text": "The shape inference of {op_name} type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function."
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Node is missing ONNX shape inference."""

    missing_custom_symbolic_function: _MissingCustomSymbolicFunction = (
        dataclasses.field(
            default=_MissingCustomSymbolicFunction.from_sarif(
                id="POE0002",
                name="missing-custom-symbolic-function",
                short_description={
                    "text": "Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX."
                },
                full_description={
                    "text": "Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX.",
                    "markdown": "Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX.\n",
                },
                message_strings={
                    "default": {
                        "text": "ONNX export failed on an operator with unrecognized namespace {op_name}. If you are trying to export a custom operator, make sure you registered it with the right domain and version."
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX."""

    missing_standard_symbolic_function: _MissingStandardSymbolicFunction = (
        dataclasses.field(
            default=_MissingStandardSymbolicFunction.from_sarif(
                id="POE0003",
                name="missing-standard-symbolic-function",
                short_description={
                    "text": "Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX."
                },
                full_description={
                    "text": "Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX.",
                    "markdown": "Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX.\n",
                },
                message_strings={
                    "default": {
                        "text": "Exporting the operator '{op_name}' to ONNX opset version {opset_version} is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub: {issue_url}."
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX."""

    operator_supported_in_newer_opset_version: _OperatorSupportedInNewerOpsetVersion = (
        dataclasses.field(
            default=_OperatorSupportedInNewerOpsetVersion.from_sarif(
                id="POE0004",
                name="operator-supported-in-newer-opset-version",
                short_description={
                    "text": "Operator is supported in newer opset version."
                },
                full_description={
                    "text": "Operator is supported in newer opset version.",
                    "markdown": "Operator is supported in newer opset version.\n\nExample:\n```python\ntorch.onnx.export(model, args, ..., opset_version=9)\n```\n",
                },
                message_strings={
                    "default": {
                        "text": "Exporting the operator '{op_name}' to ONNX opset version {opset_version} is not supported. Support for this operator was added in version {supported_opset_version}, try exporting with this version."
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Operator is supported in newer opset version."""

    fx_graph_to_onnx: _FxGraphToOnnx = dataclasses.field(
        default=_FxGraphToOnnx.from_sarif(
            id="FXE0007",
            name="fx-graph-to-onnx",
            short_description={"text": "Transforms graph from FX IR to ONNX IR."},
            full_description={
                "text": "Transforms graph from FX IR to ONNX IR.",
                "markdown": "This diagnostic tracks the transformation process from an FX Graph (in FX IR) to an ONNX Graph (in ONNX IR).\n\n## Key Representations:\n\n- **FX Graph**: The graph in FX IR produced by dynamo or symbolic tracing.\n- **ONNX Graph**: The graph in ONNX IR and [operators](https://onnx.ai/onnx/operators/).\n\n## Additional Notes:\n\n- Prior to this transformation step, the FX graph undergoes preprocessing through multiple FX passes.\n  To gain insight into these transformations, refer to diagnostic `FXE0010`.\n- To enable a detailed view of the graph transformation in progress within this diagnostic, switch to the DEBUG mode.\n\n  - Set DiagnosticOptions.verbosity_level to logging.DEBUG.\n  - Activate the environment variable TORCH_LOGS='onnx_diagnostics'.\n\n- For specific information related to node-level FX to ONNX transformations, explore the diagnostic `FXE0008`.\n",
            },
            message_strings={
                "default": {"text": "Transforming FX graph {graph_name} to ONNX graph."}
            },
            help_uri=None,
            properties={"deprecated": False, "tags": []},
        ),
        init=False,
    )
    """Transforms graph from FX IR to ONNX IR."""

    fx_node_to_onnx: _FxNodeToOnnx = dataclasses.field(
        default=_FxNodeToOnnx.from_sarif(
            id="FXE0008",
            name="fx-node-to-onnx",
            short_description={"text": "Transforms an FX node to an ONNX node."},
            full_description={
                "text": "Transforms an FX node to an ONNX node.",
                "markdown": "This diagnostic tracks the transformation process from an FX Node to ONNX [Operators](https://onnx.ai/onnx/operators/).\n\nThe process of converting FX Node to ONNX Node involves dealing with six distinct node types:\n  1. `placeholder`: Represents a module input, maps to an ONNX graph input.\n  2. `call_module`: Symbolizes a call to a submodule, maps to an ONNX\n  3. `call_method`: Symbolizes a method call. Not yet implemented.\n  4. `call_function`: Symbolizes a function call. [Core ATen](https://pytorch.org/docs/stable/ir.html#core-aten-ir) is expected\n    as the function call target. The mapping from ATen to ONNX is implemented by [ONNXScript torchlib](https://github.com/microsoft/onnxscript/tree/main/onnxscript/function_libs/torch_lib/ops).\n    This [guide](https://pytorch.org/docs/stable/onnx.html#onnx-script-functions) shows how to write and register a custom symbolic function for call_function FX node.\n  5. `get_attr`: Indicates an attribute access within the current module. Maps to an ONNX graph initializer.\n  6. `output`: Represents the module's output. Maps to an ONNX graph output.\n\nFor a granular understanding of how each node type is transformed, refer to the implementation details in `FxOnnxInterpreter`.\n",
            },
            message_strings={
                "default": {"text": "Transforming FX node {node_repr} to ONNX node."}
            },
            help_uri=None,
            properties={"deprecated": False, "tags": []},
        ),
        init=False,
    )
    """Transforms an FX node to an ONNX node."""

    fx_pass: _FxPass = dataclasses.field(
        default=_FxPass.from_sarif(
            id="FXE0010",
            name="fx-pass",
            short_description={
                "text": "FX graph transformation during ONNX export before converting from FX IR to ONNX IR."
            },
            full_description={
                "text": "FX graph transformation during ONNX export before converting from FX IR to ONNX IR.",
                "markdown": "This diagnostic tracks the FX passes executed during the ONNX export process prior\nto converting from FX IR (Intermediate Representation) to ONNX IR.\n\nUnder the scope of ONNX export, an FX pass refers to a specific transformation applied to the FX GraphModule.\nThe primary aim of these passes is to streamline the graph into a format that aligns more with the ONNX IR.\nMoreover, these passes work to substitute unsupported FX IR features with those recognized and endorsed by\nONNX IR. Common transformations include, but aren't limited to, decomposition, functionalization and\ntype promotion.\n\nFor those who are interested in a comprehensive log detailing the modifications made during these passes,\nthere are a couple of options:\n\n- Set DiagnosticOptions.verbosity_level to logging.DEBUG.\n- Activate the environment variable TORCH_LOGS='onnx_diagnostics'.\n\nHowever, it's noteworthy that by default, such detailed logging is turned off. The primary reason being\nits considerable impact on performance.\n\nFor an in-depth understanding of each specific pass, please refer to the directory: torch/onnx/_internal/fx/passes.\n",
            },
            message_strings={"default": {"text": "Running {pass_name} pass."}},
            help_uri=None,
            properties={"deprecated": False, "tags": []},
        ),
        init=False,
    )
    """FX graph transformation during ONNX export before converting from FX IR to ONNX IR."""

    no_symbolic_function_for_call_function: _NoSymbolicFunctionForCallFunction = (
        dataclasses.field(
            default=_NoSymbolicFunctionForCallFunction.from_sarif(
                id="FXE0011",
                name="no-symbolic-function-for-call-function",
                short_description={
                    "text": 'Cannot find symbolic function to convert the "call_function" FX node to ONNX.'
                },
                full_description={
                    "text": 'Cannot find symbolic function to convert the "call_function" FX node to ONNX. ',
                    "markdown": 'This error occurs when the ONNX converter is unable to find a corresponding symbolic function\nto convert a "call_function" node in the input graph to its equivalence in ONNX. The "call_function"\nnode represents a normalized function call in PyTorch, such as "torch.aten.ops.add".\n\nTo resolve this error, you can try one of the following:\n\n- If exists, apply the auto-fix suggested by the diagnostic. TODO: this part is not available yet.\n- Rewrite the model using only supported PyTorch operators or functions.\n- Follow this [guide](https://pytorch.org/tutorials/beginner/onnx/onnx_registry_tutorial.html#overview) to write and\n  register a custom symbolic function for the unsupported call_function FX node.\n',
                },
                message_strings={
                    "default": {
                        "text": 'No symbolic function to convert the "call_function" node {target} to ONNX. '
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Cannot find symbolic function to convert the "call_function" FX node to ONNX."""

    unsupported_fx_node_analysis: _UnsupportedFxNodeAnalysis = dataclasses.field(
        default=_UnsupportedFxNodeAnalysis.from_sarif(
            id="FXE0012",
            name="unsupported-fx-node-analysis",
            short_description={
                "text": "Result from FX graph analysis to reveal unsupported FX nodes."
            },
            full_description={
                "text": "Result from FX graph analysis to reveal unsupported FX nodes.",
                "markdown": "This error indicates that an FX graph contains one or more unsupported nodes. The error message\nis typically accompanied by a list of the unsupported nodes found during analysis.\n\nTo resolve this error, you can try resolving each individual unsupported node error by following\nthe suggestions by its diagnostic. Typically, options include:\n\n- If exists, apply the auto-fix suggested by the diagnostic. TODO: this part is not available yet.\n- Rewrite the model using only supported PyTorch operators or functions.\n- Follow this [guide](https://pytorch.org/docs/stable/onnx.html#onnx-script-functions) to write and\n  register a custom symbolic function for the unsupported call_function FX node.\n",
            },
            message_strings={
                "default": {
                    "text": "Unsupported FX nodes: {node_op_to_target_mapping}. "
                }
            },
            help_uri=None,
            properties={"deprecated": False, "tags": []},
        ),
        init=False,
    )
    """Result from FX graph analysis to reveal unsupported FX nodes."""

    op_level_debugging: _OpLevelDebugging = dataclasses.field(
        default=_OpLevelDebugging.from_sarif(
            id="FXE0013",
            name="op-level-debugging",
            short_description={
                "text": "Report any op level validation failure in warnings."
            },
            full_description={
                "text": "Report any op level validation failure in warnings.",
                "markdown": "This warning message indicates that during op level debugging, certain symbolic functions\nhave failed to match the results of torch ops when using real tensors generated from fake\ntensors. It is important to note that the symbolic functions may not necessarily be\nincorrect, as the validation process is non-deterministic and should only be used as a\nreference.\n\nThere are two categories of warnings that can be triggered:\n\n1. Non-validated operators:\n  If the warnings are caused by the following errors, they can be disregarded by users,\n  as these errors occur due to the non-deterministic nature of the validation. However,\n  it is important to be aware that the operators have not been validated.\n\n  - IndexError: Unsupported input arguments of randomized dimensions/indices(INT64).\n  - RuntimeError: Unsupported input arguments for torch ops are generated.\n  - ValueError: Arguments/keyword arguments do not match the signature of the symbolic function.\n\n2. Potentially wrong torchlib operators:\n  If the warnings are triggered by the following error, users should be aware that the symbolic functions\n  may be incorrect in dispatching or implementation. In such cases, it is recommended to report\n  the issue to the PyTorch-ONNX team, or create/register a custom symbolic function to replace the default one.\n\n  - AssertionError: The symbolic function is potentially wrong as the results do not match the results of torch ops.\n  - TypeError: The symbolic function is potentially wrong as the opschema doesn't match inputs.\n",
            },
            message_strings={
                "default": {
                    "text": "FX node: {node} and its onnx function: {symbolic_fn} fails on op level validation."
                }
            },
            help_uri=None,
            properties={"deprecated": False, "tags": []},
        ),
        init=False,
    )
    """Report any op level validation failure in warnings."""

    find_opschema_matched_symbolic_function: _FindOpschemaMatchedSymbolicFunction = (
        dataclasses.field(
            default=_FindOpschemaMatchedSymbolicFunction.from_sarif(
                id="FXE0014",
                name="find-opschema-matched-symbolic-function",
                short_description={
                    "text": "Find the OnnxFunction that matches the input/attribute dtypes by comparing them with their opschemas."
                },
                full_description={
                    "text": "Find the OnnxFunction that matches the input dtypes by comparing them with their opschemas. A warning will be issued if the matched OnnxFunction is not an exact match.",
                    "markdown": "When an ATen/Custom operator is registered and needs to be dispatched to an OnnxFunction, the input/attribute\ndtypes of the ATen/Custom operator are compared with the input/attribute dtypes of the OnnxFunction opschemas\nto find a match. However, if a perfect/exact match is not found, the dispatcher will attempt to find\nthe nearest match with the highest number of input/attribute dtypes matching the OnnxFunction opschemas, while\nissuing a warning.\n\nThere are two types of level that can be triggered in this rule:\n\n1. NOTE: A perfect match is found, and no warning is issued.\n2. WARNING: The matched OnnxFunction is not a perfect/exact match.\n\nHere are some suggestions based on the WARNING situation:\n\n1. If there are NO errors or mismatches in the results, it is safe to disregard this warning,\n  as the definition of OnnxFunction schema is usually more stringent.\n2. If there are errors or mismatches in the results, it is recommended to:\n  (a) Enable op_level_debugging to determine if the OnnxFunction might be incorrect.\n  (b) Report the issue to the PyTorch-ONNX team.\n  (c) Create/register a custom symbolic function to replace the default one.\n",
                },
                message_strings={
                    "default": {
                        "text": "The OnnxFunction: {symbolic_fn} is the nearest match of the node {node}."
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Find the OnnxFunction that matches the input/attribute dtypes by comparing them with their opschemas."""

    fx_node_insert_type_promotion: _FxNodeInsertTypePromotion = dataclasses.field(
        default=_FxNodeInsertTypePromotion.from_sarif(
            id="FXE0015",
            name="fx-node-insert-type-promotion",
            short_description={
                "text": "Determine if type promotion is required for the FX node. Insert cast nodes if needed."
            },
            full_description={
                "text": "Determine if type promotion is required for the FX node. Insert cast nodes if needed.",
                "markdown": "This diagnostic monitors the node-level type promotion insertion process. In PyTorch, there is an automatic process called implicit type promotion,\nwhere the input types of an operator are promoted to a common type. The determination of the common type is based on the type promotion rule specific to each operator.\nTo learn more about PyTorch's type promotion rules, refer to the [elementwise_dtypes doc](https://github.com/pytorch/pytorch/blob/f044613f78df713fb57f70c608483c9f10ad332e/torch/_prims_common/__init__.py#L1252-L1335)\nand [torch._refs ops](https://github.com/pytorch/pytorch/blob/a475ea4542dfe961c9d097e33ab5041f61c8c17f/torch/_refs/__init__.py#L484).\n\nHowever, implicit type promotion is not supported in ONNX. Therefore, to replicate the PyTorch behavior, we need to explicitly insert cast nodes.\nThis diagnostic tracks the process of node-level type promotion insertion.\n\nThe type promotion rules used by this process can be found in `torch/onnx/_internal/fx/passes/type_promotion.py.`\nTo update or add new type promotion rules, please refer to the [Note: Update type promotion rule] section.\n",
            },
            message_strings={
                "default": {
                    "text": "Performing explicit type promotion for node {target}. "
                }
            },
            help_uri=None,
            properties={"deprecated": False, "tags": []},
        ),
        init=False,
    )
    """Determine if type promotion is required for the FX node. Insert cast nodes if needed."""

    find_operator_overloads_in_onnx_registry: _FindOperatorOverloadsInOnnxRegistry = (
        dataclasses.field(
            default=_FindOperatorOverloadsInOnnxRegistry.from_sarif(
                id="FXE0016",
                name="find-operator-overloads-in-onnx-registry",
                short_description={
                    "text": "Find the list of OnnxFunction of the PyTorch operator in onnx registry."
                },
                full_description={
                    "text": "This rule involves finding the list of OnnxFunction for the PyTorch operator overload in the ONNX registry. If the operator overload is not supported but its default overload is, a warning will be issued. If both the operator overload and its default overload are not supported, an error will be issued.",
                    "markdown": "The operator overload name serves the purpose of verifying whether a PyTorch operator is registered in the ONNX registry.\nIf it's not found, the dispatcher takes a fallback approach and tries to locate the default overload of the PyTorch\noperator in the registry. If even the default overload is absent, it signifies that the operator is officially unsupported.\n\nThere are three types of level that can be triggered in this rule:\n\n1. NOTE: The op overload is supported.\n2. WARNING: The op overload is not supported, but it's default overload is supported.\n3. ERROR: The op overload is not supported, and it's default overload is also not supported.\n\nHere are some suggestions based on the WARNING situation:\n\n1. If there are NO errors or mismatches in the results, it is safe to disregard this warning.\n2. If there are errors or mismatches in the results, it is recommended to:\n  (a) Enable op_level_debugging to determine if the OnnxFunction might be incorrect.\n  (b) Report the unsupported overload to the PyTorch-ONNX team.\n  (c) Create/register a custom symbolic function to replace the default one.\n\nHere are some suggestions based on the ERROR situation:\n\n1. Report the unsupported operator to the PyTorch-ONNX team.\n2. Create/register a custom symbolic function to replace the default one.\n",
                },
                message_strings={
                    "default": {
                        "text": "Checking if the FX node: {node} is supported in onnx registry."
                    }
                },
                help_uri=None,
                properties={"deprecated": False, "tags": []},
            ),
            init=False,
        )
    )
    """Find the list of OnnxFunction of the PyTorch operator in onnx registry."""


rules = _POERules()
