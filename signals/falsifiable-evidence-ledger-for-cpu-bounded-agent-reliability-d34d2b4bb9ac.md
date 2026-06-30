# Falsifiable Evidence Ledger for CPU-Bounded Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-for-cpu-bounded-agent-reliability-d34d2b4bb9ac`
Run ID: `falsifiable-evidence-ledger-for-cpu-bounded-agent-reliability-d34d2b4bb9ac-20260614T010431957343+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c17567e767f8

## What looked useful

A strict claim-to-evidence observation matcher accepted all 18 supported claims and rejected all 17 trap claims, while a schema/reference-existence baseline false-accepted 13 of 17 unsupported trap claims.

## Boundaries and scale limits

Synthetic structured claims only; no real agent traces, no noisy natural-language extraction, no adversarial evidence paraphrases, no multi-run variance, and no large heterogeneous task corpus.

## Claim scope

On a deterministic synthetic structured-ledger benchmark with 35 claims, exact evidence-grounding eliminated unsupported-claim false accepts that remained after schema and evidence-reference-existence checks.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic mechanism evidence rather than full validation of real-world agent reliability.

## Recommended next action

Run a bounded real-trace follow-up using CPU-bounded agent logs with hidden drift/trap labels and compare false accept/reject rates against the same schema/ref baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence ledger gate for CPU-bounded agent drift traps
- Success threshold: Strict grounding reduces unsupported-claim false accept rate by >=50% relative to schema/ref baseline and keeps supported-claim false reject rate <=10% on the labeled trace corpus.
- Stop condition: Stop if strict grounding has >10% supported-claim false rejects or <25% false-accept reduction after the first labeled 50-trace corpus.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-cpu-bounded-agent-reliability-d34d2b4bb9ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
