# Evidence Ledger Reduces Tool Misuse in 1B CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reduces-tool-misuse-in-1b-cpu-agents-a5a41a1f661f`
Run ID: `evidence-ledger-reduces-tool-misuse-in-1b-cpu-agents-a5a41a1f661f-20260528T022613356734+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/323a2ef4999d

## What looked useful

Main 5,000-episode paired run: baseline misuse 0.7332, append-only ledger 0.7054, verifier-only 0.0260, full evidence ledger 0.0018 with 0.0382 abstention. Sensitivity sweep preserved low ledger misuse under verifier false-accept rates up to 0.20.

## Boundaries and scale limits

No real 1B-parameter CPU model, natural-language prompt-following, production tool framework, latency/cost profile, or adversarial held-out benchmark was tested. The result is mechanism evidence only.

## Claim scope

In a deterministic synthetic agent-harness benchmark with matched paired episodes, enforceable evidence-ledger gating reduced stale/untrusted/irrelevant tool-evidence misuse compared with a noisy baseline, append-only ledger logging, and verifier-only repair.

## Why it stopped

Stopped after a bounded synthetic mechanism test; evidence is useful but not paper-ready because it does not directly validate 1B CPU agents.

## Recommended next action

Run a bounded real-model follow-up using a quantized 1B-class CPU agent on natural-language tool tasks with the same baseline, append-only ledger, verifier-only, and full-ledger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real 1B CPU Agent Evidence-Ledger Tool-Misuse Benchmark
- Success threshold: Full evidence-ledger condition achieves at least 50% relative misuse reduction versus verifier-only and at least 80% relative reduction versus baseline, with abstention below 15% and median latency overhead below 2x baseline.
- Stop condition: Stop as negative if the 1B model fails to maintain usable ledger entries in more than 25% of tasks, or if full-ledger misuse is not lower than verifier-only by at least 10% relative after 200 paired tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-tool-misuse-in-1b-cpu-agents-a5a41a1f661f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
