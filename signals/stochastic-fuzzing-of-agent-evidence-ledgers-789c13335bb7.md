# Stochastic Fuzzing of Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7`
Run ID: `stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7-20260527T212213127006+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ca1df01e51ec

## What looked useful

A 5,000-trial campaign found detection rates of 0.0000 for schema-only validation, 0.2282 for hash-chain-only validation, and 0.8854 for semantic validation, with zero valid-control false rejects. Five replicate seeds showed stable means of 0.0000, 0.2203, and 0.8909 respectively. Rehashed claim-text rewrite remained undetected without external immutability or entailment checks.

## Boundaries and scale limits

Evidence is limited to synthetic ledgers, hand-authored mutation families, single-process CPU fuzzing, and structural semantic checks. It does not test real agent frameworks, signed append-only storage, concurrent writers, production evidence traces, or natural-language entailment of rewritten claims.

## Claim scope

In a synthetic append-only agent evidence-ledger harness, stochastic mutation testing separates schema-only, hash-chain-only, and semantic validators; hash-chain-only validation misses rehashed semantic corruptions while semantic invariants detect 8 of 9 generated mutation families.

## Why it stopped

Synthetic evidence supports the mechanism but is not direct/full validation; publication-grade claims would require real ledger implementations, persistence/signing checks, and natural-language evidence-quality tests.

## Recommended next action

Run the same mutation families against a real agent evidence-ledger implementation with signed snapshots and task-derived traces; stop this run as no-paper synthetic useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fuzz a Real Signed Agent Evidence Ledger
- Success threshold: On at least 1,000 mutated real-trace ledgers, semantic plus signature/snapshot-aware validation detects at least 95% of generated corruptions with no more than 1% false rejects on valid traces, and detects rehashed claim-text rewrites that the current semantic-only harness cannot detect.
- Stop condition: Stop if no real ledger or signed snapshot implementation is available locally, or if valid real traces produce more than 5% false rejects after one validator calibration pass.

## Evidence references

- Artifact root: `<local-path>/projects/stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
