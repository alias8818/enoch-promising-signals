# Real LLM Repeated-Instruction Doctrine vs Trace Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-llm-repeated-instruction-doctrine-vs-trace-retrieval-a972f9c1d3`
Run ID: `real-llm-repeated-instruction-doctrine-vs-trace-retrieval-a972f9c1d3-20260628T211803796941+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Doctrinal Memory vs Retrieval-Only on Repeated Tasks: enoch://control-plane/projects/doctrinal-memory-vs-retrieval-only-on-repeated-tasks-8281f76b813a/runs/doctrinal-memory-vs-retrieval-only-on-repeated-tasks-8281f76b813a-20260628T210431921141+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9213839e1be7

## What looked useful

Repeated instruction did not show a general doctrine advantage over near-query trace retrieval: repeated_rule compliance was 30/120 (25.0%) and trace_near was 31/120 (25.8%), with paired repeated-only 11 vs trace-only 12. A single clean top-level rule was stronger at 58/120 (48.3%), suggesting repeated context can add clutter rather than strengthen compliance in this setup.

## Boundaries and scale limits

No training or persistence test; no external retriever; synthetic tasks only; prompt lengths were not token-matched; model set was limited to locally cached 135M-1.7B class open models plus Qwen 0.5B/1.5B; one cached SmolLM2 360M model was excluded due load failure.

## Claim scope

Bounded local in-context behavioral probe across five cached instruction-tuned causal LMs, 24 synthetic adversarial code-word tasks, and four prompt conditions comparing single top instruction, repeated instruction, near-query trace cue, and repeated instruction with conflicting trace.

## Why it stopped

Proxy/local behavioral evidence is mixed against the repeated-instruction doctrine advantage and is not a full validation or full falsification of durable doctrine claims.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a token-matched deepen experiment with randomized instruction placement and an external retriever-inserted trace control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-matched repeated instruction versus trace retrieval controls
- Success threshold: Support for repeated-instruction doctrine requires repeated-rule compliance at least 15 percentage points above both token-matched filler and trace-near controls on at least two model families; otherwise treat the doctrine advantage as unsupported for in-context behavior.
- Stop condition: Stop if repeated-rule compliance is within 5 percentage points of trace/filler controls or remains below single-top instruction performance after 100 cases per condition.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-repeated-instruction-doctrine-vs-trace-retrieval-a972f9c1d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
