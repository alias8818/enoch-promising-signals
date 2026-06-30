# Ledger-backed tool-call verification with local tiny LLM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ledger-backed-tool-call-verification-with-local-tiny-llm-7729147f4106`
Run ID: `ledger-backed-tool-call-verification-with-local-tiny-llm-7729147f4106-20260531T100630902097+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

Transcript-only tiny LM reached F1 0.7098. Ledger-backed tiny LM reached F1 0.8948. Deterministic ledger with final-root anchor reached F1 0.9026 but missed all 52 valid-hash semantic lies. Unanchored ledger checks missed all 54 recomputed ledgers. Deterministic ledger plus exact semantic checks reached F1 1.0000 on this synthetic benchmark.

## Boundaries and scale limits

Synthetic generated traces only; local verifier is a character n-gram language-model classifier rather than a downloaded pretrained neural tiny LLM; tool domains have simple deterministic semantics; no real production agent traces, adversarial prompts, external transparency log, or multi-session deployment were tested.

## Claim scope

On a synthetic 600-example test set of 5-step tool-call ledgers, final-root anchoring improves tamper detection over unanchored ledger checks, ledger-verifier signals improve a tiny local n-gram audit model over transcript-only auditing, and pure ledger checks miss semantically false tool results committed into valid ledgers.

## Why it stopped

Synthetic proxy run produced useful mechanism evidence and clear failure modes, but it is not a full validation of ledger-backed verification with a neural local tiny LLM.

## Recommended next action

Run a bounded deepen follow-up with an actual local neural tiny LLM, fixed prompts, and held-out real or realistic agent traces; do not write a paper from this proxy-only run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LLM verifier on anchored real tool-call ledgers
- Success threshold: Ledger-backed neural tiny LLM improves semantic-lie recall by at least 15 percentage points over transcript-only prompting while keeping clean-trace false-positive rate below 5%, and deterministic ledger anchoring catches at least 99% of structural tampering in the tested trace set.
- Stop condition: Stop if the neural tiny LLM cannot beat transcript-only F1 by at least 0.05 or if clean-trace false-positive rate exceeds 10% after fixed prompt calibration.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-backed-tool-call-verification-with-local-tiny-llm-7729147f4106`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
