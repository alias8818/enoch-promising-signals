# Evidence-Ledger Reliability Test on CPU-Backed Tiny Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reliability-test-on-cpu-backed-tiny-agent-5d8fbb54e356`
Run ID: `evidence-ledger-reliability-test-on-cpu-backed-tiny-agent-5d8fbb54e356-20260629T071311946673+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed5246c3b5cb

## What looked useful

The scaffold can be turned into a reproducible local reliability harness. In this bounded run, ledger checks caught 48/48 injected invalid rows and accepted 12/12 valid rows, yielding 0.0 false accept and 0.0 false reject rates under the synthetic oracle.

## Boundaries and scale limits

Synthetic exact-match workload only; no real LLM, no naturalistic tool traces, no paraphrase acceptance test, no multi-hop evidence, and no large-scale hidden-drift benchmark.

## Claim scope

On a seeded 60-row synthetic fact-extraction workload, a deterministic evidence-ledger verifier rejected simple wrong-answer, missing-evidence, bad-quote, and stale-hash faults from a CPU-only tiny agent while accepting valid exact-match rows.

## Why it stopped

No-paper closure: the current result is a useful synthetic mechanism signal, not direct publication-grade evidence for real agent reliability.

## Recommended next action

Run a bounded real-agent follow-up with paraphrased evidence and hidden-drift task traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Agent Evidence Ledger With Paraphrase and Hidden Drift
- Success threshold: False accept rate below 5% on invalid/trap rows and false reject rate below 10% on valid rows, with at least 100 labeled traces.
- Stop condition: Stop if false accepts are 10% or higher after the first 50 labeled real-agent traces, or if valid paraphrases cause false rejects above 20%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reliability-test-on-cpu-backed-tiny-agent-5d8fbb54e356`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
