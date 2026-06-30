# Human or model authored external anchors for live trace resumption

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `human-or-model-authored-external-anchors-for-live-trace-re-12b5ae1d91`
Run ID: `human-or-model-authored-external-anchors-for-live-trace-re-12b5ae1d91-20260529T165131091339+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Externally Persisted Anchors Across Multiple Real Agent Traces: enoch://control-plane/projects/externally-persisted-anchors-across-multiple-real-agent-tr-dfea073862/runs/externally-persisted-anchors-across-multiple-real-agent-tr-dfea073862-20260529T132620968499+0000
- Parent run decision: Anchored Hash-Chain Provenance on Real Agent Traces: enoch://control-plane/projects/anchored-hash-chain-provenance-on-real-agent-traces-4dbc1c3774/runs/anchored-hash-chain-provenance-on-real-agent-traces-4dbc1c3774-20260529T093553434652+0000

## What looked useful

Main run: clipped trace only reached 0.4005 item accuracy, 0.7112 next-action accuracy, and 0.0000 exact-state recovery; oracle anchors reached 1.0000 on all three; noisy extractive anchors reached 0.8286 item accuracy, 0.9447 next-action accuracy, and 0.2195 exact-state recovery. Shuffled anchors almost never recovered exact state (0.0005), supporting that anchor content matters.

## Boundaries and scale limits

50,000 generated cases plus five 5,000-case sensitivity runs on a CPU worker. Human-authored anchors were oracle structured state, model-authored anchors were deterministic noisy/extractive proxies, and resumption used a deterministic parser rather than a live LLM agent on real traces.

## Claim scope

In a fixed-seed synthetic live-trace resumption benchmark with known task state, external anchors materially improve hard-cutover state and next-action recovery over clipped recent trace context. Complete oracle/human-style anchors recover the synthetic state exactly, and noisy extractive model-style anchors improve item accuracy and next-action accuracy but do not reliably recover exact full state.

## Why it stopped

The benchmark directly supports the anchor mechanism under synthetic controlled conditions, but publication readiness would require actual human/model-authored anchors and live or replayed LLM agent resumption rather than proxies.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use actual human-written and LLM-written anchors on real or replayed agent traces with blinded LLM resumption.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded LLM resumption with real human and model-authored anchors
- Success threshold: Across at least 200 interrupted traces, human or LLM anchors improve next-action correctness by at least 15 percentage points over clipped trace only, shuffled anchors do not exceed clipped trace by more than 5 percentage points, and human/structured anchors improve exact state recovery by at least 20 percentage points over unstructured model anchors.
- Stop condition: Stop if real anchors fail to beat clipped trace by 5 percentage points on next-action correctness or if shuffled anchors match real anchors, because that would falsify the content-specific anchor mechanism in the live-resumption setting.

## Evidence references

- Artifact root: `<local-path>/projects/human-or-model-authored-external-anchors-for-live-trace-re-12b5ae1d91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
