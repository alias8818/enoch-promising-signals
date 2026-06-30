# Counterexample Mining: Systematic Falsification of Agent Evidence Ledger Claims

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `counterexample-mining-systematic-falsification-of-agent-evidence-ledger-claims-251170182831`
Run ID: `counterexample-mining-systematic-falsification-of-agent-evidence-ledger-claims-251170182831-20260611T072353214588+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2d662c61c743

## What looked useful

Four ledgers passed schema and existence/hash validation while failing semantic recomputation; one control passed semantic recomputation. This falsifies structural-check sufficiency for the scoped synthetic ledger model.

## Boundaries and scale limits

Five synthetic ledger entries only; no production agent ledgers, external benchmark artifacts, or prevalence estimate. CPU-only local run under one minute.

## Claim scope

Synthetic local evidence-ledger entries show that schema, path-existence, and SHA-256 artifact checks do not by themselves verify metric, evaluation-scope, configuration, or quantifier claims.

## Why it stopped

Synthetic/proxy early falsification of structural ledger sufficiency, not a full validation of real-world agent ledger prevalence.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should apply the same semantic validators to a small corpus of real agent evidence ledgers with executable artifacts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate semantic overclaim detection on real agent evidence ledgers
- Success threshold: At least 10 percent of structurally valid ledgers fail semantic validation with manually confirmed overclaim reasons, while at least one known-good control ledger passes.
- Stop condition: Stop if fewer than 20 executable ledgers can be obtained locally, if artifacts are unavailable, or if semantic validator errors exceed confirmed overclaims.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-mining-systematic-falsification-of-agent-evidence-ledger-claims-251170182831`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
