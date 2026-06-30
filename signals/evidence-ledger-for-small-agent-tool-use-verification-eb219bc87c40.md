# Evidence Ledger for Small Agent Tool-Use Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40`
Run ID: `evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40-20260525T143821026652+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2348c1aa266a

## What looked useful

The ledger verifier achieved 1.000 invalid detection and 0.000 false accept rate on controlled synthetic corruptions; reexecution-only and transcript-keyword baselines false-accepted about 0.592 and 0.624 of invalid cases in five replicate seeds. This supports the ledger mechanism as a useful next test target, not a paper-ready claim.

## Boundaries and scale limits

No real LLM agent traces, nondeterministic external tools, streaming outputs, side-effectful actions, prompt injection, human audit UX, or strong semantic transcript verifier were tested. The result should not be extrapolated to deployed agent systems without direct trace validation.

## Claim scope

In a synthetic deterministic small-tool harness, a typed append-only hash-chained evidence ledger verified tool-use claims and rejected all tested claim, transcript, schema, omission, and ledger-tamper corruptions across 9,000 medium-run episodes plus five 3,000-episode replicate seeds.

## Why it stopped

Proxy/synthetic evidence supports the mechanism but is insufficient for publication-grade validation of real small-agent tool-use verification.

## Recommended next action

Run a bounded real-trace follow-up using small local or API agents with captured tool observations and a stronger semantic transcript/audit baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Agent Trace Validation for Evidence Ledgers
- Success threshold: Ledger false accept rate at least 50% lower than the best non-ledger baseline, absolute false reject rate no more than 2% on honest traces, and no undetected ledger-tamper cases in the injected corruption set.
- Stop condition: Stop as negative if ledger verification false-rejects more than 5% of honest real traces or fails to outperform the best non-ledger baseline by at least 20% relative false-accept reduction.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
