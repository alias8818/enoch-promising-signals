# Evidence-ledger counterexample traces on recorded tool-agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-counterexample-traces-on-recorded-tool-age-030cc165f2`
Run ID: `evidence-ledger-counterexample-traces-on-recorded-tool-age-030cc165f2-20260621T022902418207+0000`

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

- Parent run decision: Evidence-Ledger Agent: Falsifiable Claims with Counterexample Traces: enoch://control-plane/projects/evidence-ledger-agent-falsifiable-claims-with-counterexample-traces-b42178741090/runs/evidence-ledger-agent-falsifiable-claims-with-counterexample-traces-b42178741090-20260621T012643812159+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d322eaea04a2

## What looked useful

The verifier achieved 8/8 counterexample detections, 0 false accepts, and 0 false rejects across 16 claims, outperforming an accept-all transcript baseline that would miss all 8 counterexamples.

## Boundaries and scale limits

Small synthetic controlled corpus; structured assertions only; no natural-language claim extraction, noisy evidence, multi-hop evidence, adversarial paraphrase, or large real-world trace corpus was tested.

## Claim scope

In a controlled Tier 1 corpus of 8 recorded tool-agent traces with explicit tool observations and structured final-claim assertions, an evidence-ledger verifier detected all injected direct counterexamples while accepting all supported claims.

## Why it stopped

Tier 1 controlled direct test completed with useful mechanism support, but evidence remains too small and structured for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on 30 to 50 real or realistic recorded tool-agent traces with blinded labels and a separate natural-language claim extraction step before considering paper framing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger counterexample detection on realistic recorded agent traces
- Success threshold: Counterexample detection rate >= 0.80 and supported-claim false reject rate <= 0.10 on the labeled realistic trace set.
- Stop condition: Stop as negative if detection is below 0.60, if false reject rate exceeds 0.25, or if claim extraction cannot produce auditable evidence references for at least 80% of traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-counterexample-traces-on-recorded-tool-age-030cc165f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
