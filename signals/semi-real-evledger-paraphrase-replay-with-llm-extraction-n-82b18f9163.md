# Semi-real EvLedger paraphrase replay with LLM extraction noise

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `semi-real-evledger-paraphrase-replay-with-llm-extraction-n-82b18f9163`
Run ID: `semi-real-evledger-paraphrase-replay-with-llm-extraction-n-82b18f9163-20260619T222001020263+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Held-out multi-session EvLedger paraphrase replay: enoch://control-plane/projects/held-out-multi-session-evledger-paraphrase-replay-2e196d677e/runs/held-out-multi-session-evledger-paraphrase-replay-2e196d677e-20260619T215852386031+0000
- Parent run decision: Replay EvLedger on real repeated tool-agent traces with paraphrase drift: enoch://control-plane/projects/replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862/runs/replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862-20260619T214300934539+0000

## What looked useful

Preserving raw transcript evidence and using consistency voting recovered high accuracy under severe extraction noise: layered_doctrine_memory reached 0.9861 overall mean accuracy versus 0.6694 for flat_retrieval and 0.6871 for the no-consistency ablation. The transcript_search baseline reached 1.0000, so the stronger research claim is not supported.

## Boundaries and scale limits

Synthetic templated ledger records, simulated extractor noise rather than live LLM outputs, exact event-id query shortcut, single-process CPU run, 8 seeds, 7 noise levels, 1,120,000 scored queries.

## Claim scope

In a deterministic synthetic EvLedger replay with exact event ids in paraphrased queries and probabilistic extraction-noise injection, layered memory with raw-text consistency voting is robust to noisy extracted fields and beats extraction-only memory, but it does not beat raw transcript retrieval.

## Why it stopped

Mechanism supported against extractor-dependent baselines, but not against the real transcript baseline; current evidence is synthetic and not paper-positive.

## Recommended next action

Stop as no-paper useful signal; a bounded follow-up should replace simulated extraction noise with fixed LLM extractor outputs and remove exact event-id shortcuts from transcript retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: EvLedger replay without event-id shortcuts using recorded LLM extraction errors
- Success threshold: Layered_doctrine_memory exceeds both transcript_search and flat_retrieval by at least 5 absolute accuracy points on the no-event-id replay split while preserving at least 0.90 accuracy at moderate recorded extraction error rates.
- Stop condition: Stop negative if transcript_search matches or exceeds layered_doctrine_memory, or if gains disappear when recorded LLM extraction outputs replace simulated noise.

## Evidence references

- Artifact root: `<local-path>/projects/semi-real-evledger-paraphrase-replay-with-llm-extraction-n-82b18f9163`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
