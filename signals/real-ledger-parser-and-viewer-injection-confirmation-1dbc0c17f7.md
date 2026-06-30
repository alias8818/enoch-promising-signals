# Real Ledger Parser and Viewer Injection Confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-ledger-parser-and-viewer-injection-confirmation-1dbc0c17f7`
Run ID: `real-ledger-parser-and-viewer-injection-confirmation-1dbc0c17f7-20260526T225831244308+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Adversarial Ledger Injection Stress Test: enoch://control-plane/projects/adversarial-ledger-injection-stress-test-c01ccd3cde03/runs/adversarial-ledger-injection-stress-test-c01ccd3cde03-20260525T024721117707+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/746db4ff038f

## What looked useful

A real Beancount/Fava parser-to-viewer path preserves prompt-injection-like ledger text into analyst-visible and API-accessible surfaces, while Fava escaped/did not execute the HTML script probe in the tested journal view.

## Boundaries and scale limits

Single small controlled ledger fixture; one parser/viewer stack; no real bank import corpus; no downstream LLM workflow; no alternate ledger viewers or exports.

## Claim scope

In a controlled Beancount 3.2.3 ledger viewed with Fava 1.30.13, adversarial natural-language text in transaction narration and metadata survives parsing and appears in Fava viewer/API surfaces, including browser-visible journal text. The tested script-tag payload did not execute in the rendered browser journal.

## Why it stopped

Tier 1 direct test met the controlled validation target but supports only a narrow mechanism signal, not publication readiness.

## Recommended next action

Run a bounded deepen follow-up that adds one downstream LLM summarization/copy workflow and one alternate real viewer/import path, with clean-ledger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Downstream LLM Impact From Real Ledger Viewer Text
- Success threshold: Injected ledger output changes at least 3 of 5 repeated downstream summaries in the instructed direction while clean controls do not, and the propagation path is confirmed from parser to viewer to LLM input.
- Stop condition: Stop if the injected text does not reach the downstream LLM input through the real viewer workflow, or if repeated LLM outputs show no difference from clean controls.

## Evidence references

- Artifact root: `<local-path>/projects/real-ledger-parser-and-viewer-injection-confirmation-1dbc0c17f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
