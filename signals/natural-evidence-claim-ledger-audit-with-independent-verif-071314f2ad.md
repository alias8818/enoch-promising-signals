# Natural Evidence Claim-Ledger Audit with Independent Verification

Status: `useful_signal`
Project ID: `natural-evidence-claim-ledger-audit-with-independent-verif-071314f2ad`
Run ID: `natural-evidence-claim-ledger-audit-with-independent-verif-071314f2ad-20260519T140532940921+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Natural Evidence Claim-Ledger Audit with Independent Verification: internal_generated:natural-evidence-claim-ledger-audit-with-independent-verif-071314f2ad

## What looked useful

The ledger mechanism is verifier-bottlenecked: the local verifier reached 0.858 train balanced accuracy but only 0.512 held-out atomic balanced accuracy and 0.492 ROC AUC. Downstream ledger all-atoms improved balanced accuracy over whole response by only +0.025 mean, changed unsupported F1 by -0.003 mean, and trailed the shuffled-evidence control by -0.0025 balanced accuracy.

## Boundaries and scale limits

Evaluation used 894 SciFact train atomic verifier examples, 323 SciFact dev atoms, 6,000 calibration composites, and 6,000 held-out evaluation composites across five fixed seeds. Composite answers were synthetic mixtures of dataset claims, evidence documents were supplied rather than retrieved, and the verifier was lightweight rather than a pretrained NLI/LLM verifier.

## Claim scope

On SciFact-derived 2-4 atom composite answers using a locally trained TF-IDF/logistic independent verifier, atomic claim-ledger aggregation did not meet the preset unsupported-detection improvement threshold over whole-response verification and did not beat a shuffled-evidence control.

## Why it stopped

Bounded direct evaluation failed the preset success threshold: ledger did not improve unsupported F1 or balanced accuracy by 0.10 over whole-response verification and did not beat the shuffled-evidence control.

## Recommended next action

Stop this run as a no-paper bounded negative; the only justified adjacent test is to repeat the same SciFact composite protocol with a stronger independent NLI or LLM verifier and the same shuffled-evidence control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Claim-Ledger Audit with Strong Independent NLI Verification
- Success threshold: Atomic verifier ROC AUC >= 0.75 on SciFact dev; ledger all-atoms improves balanced accuracy and unsupported F1 by >= 0.10 over whole-response verification; supported recall drop <= 0.15; ledger beats shuffled-evidence control on balanced accuracy.
- Stop condition: Stop negative if atomic verifier ROC AUC remains below 0.75 or if ledger all-atoms fails either the +0.10 improvement threshold or the shuffled-evidence control.

## Evidence references

- Artifact root: `<local-path>/projects/natural-evidence-claim-ledger-audit-with-independent-verif-071314f2ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
