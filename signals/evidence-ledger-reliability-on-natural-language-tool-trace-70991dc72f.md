# Evidence-ledger reliability on natural-language tool traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-reliability-on-natural-language-tool-trace-70991dc72f`
Run ID: `evidence-ledger-reliability-on-natural-language-tool-trace-70991dc72f-20260620T221158472589+0000`

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

- Parent run decision: Evidence-Ledger Agent Reliability on Bounded Tool Traces: enoch://control-plane/projects/evidence-ledger-agent-reliability-on-bounded-tool-traces-ac4da41441cf/runs/evidence-ledger-agent-reliability-on-bounded-tool-traces-ac4da41441cf-20260620T215432137408+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

Evidence-ledger checking is mechanically useful for stale observations, contradictions, entity swaps, numeric mismatches, unsupported citations, and mixed claims when trace wording is parseable; broad natural-language reliability is not supported because lexical-stress supported recall was 0.0 and aggregate supported recall was 0.75.

## Boundaries and scale limits

Synthetic controlled traces only; no real LLM-generated traces, human-authored trace corpus, open-domain extractor, multi-hop evidence synthesis, or large-scale robustness run. CPU-only benchmark completed in under one second.

## Claim scope

Tier 1 controlled direct test on 288 generated natural-language tool traces: a typed evidence ledger beat a naive citation baseline overall and was perfect on constrained schema-like traces, but failed supported-claim recall and evidence attribution under modest lexical wording shifts.

## Why it stopped

Tier 1 direct test produced a useful but no-paper mixed result: controlled split passed, lexical-stress split failed, so broad natural-language evidence-ledger reliability is early-falsified rather than validated.

## Recommended next action

Deepen with a bounded extractor-robustness test on held-out human or LLM-authored tool traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Extractor-robust evidence ledgers on held-out natural-language tool traces
- Success threshold: On held-out traces, supported recall >= 0.85, unsupported recall >= 0.85, exact evidence attribution on supported claims >= 0.85, and overall accuracy improves over the naive citation baseline by >= 0.15 absolute.
- Stop condition: Stop as no-paper if supported recall or exact evidence attribution remains below 0.80 after adding the extractor layer, or if unsupported recall drops below 0.85.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reliability-on-natural-language-tool-trace-70991dc72f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
